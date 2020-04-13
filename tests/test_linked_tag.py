import io
import mock
import pytest
import requests
from yaml import load, dump, SafeDumper
from lnkd import LinkedTag, LinkedDumper, LinkedLoader


@pytest.fixture()
def minimal_yaml_string():
    return "name: foxtrot"


@pytest.fixture()
def docker_compose_dict():
    return {
        "version": "1",
        "services": {
            "client": {
                "restart": "always",
                "build": {
                    "image": "python:3.6.4",
                    "ports": ["8080:8080"],
                    "environment": {
                        "POSTGRES_USER": "admin",
                        "POSTGRES_PASSWORD": "1234",
                    },
                },
            }
        },
    }


@pytest.fixture()
def linked_docker_compose_dict():
    data = {
        "version": "1",
        "services": {
            "client": {"build": "!@ http://test.example.com/client/build-spec"},
            "server": {"build": "!@ relative/path/to/build-spec"},
            "db": {"build": "!@ https://test.example.com/db/build-spec"},
        },
    }
    return data


@pytest.fixture()
def yaml_string(docker_compose_dict):
    buf = io.StringIO()

    dump(docker_compose_dict, buf, default_flow_style=False, Dumper=SafeDumper)
    return buf.getvalue()


@pytest.fixture()
def linked_yaml_string(linked_docker_compose_dict):
    data = """
    services:
      client:
        build: !@ 'http://test.example.com/client/build-spec'
      server:
        build: !@ 'relative/path/to/build-spec'
    version: '1'
    """
    return data


@pytest.fixture()
def success_response(minimal_yaml_string):
    response = requests.Response()
    response.status_code = 200
    response._content = minimal_yaml_string.encode("utf-8")
    return response


def test_has_correct_interface():
    assert hasattr(LinkedTag, "symbol")
    assert hasattr(LinkedTag, "from_yaml")
    assert hasattr(LinkedTag, "to_yaml")
    assert str(LinkedTag("demo.yml")) == "!@ demo.yml"


def test_fetch_url(mocker, success_response, minimal_yaml_string):
    mocker.patch("requests.get", return_value=success_response, auto_spec=True)

    data = LinkedTag.fetch("...")

    assert isinstance(data, io.StringIO)
    assert data.read() == minimal_yaml_string


def test_linked_loader_loads_standard_yaml(yaml_string, docker_compose_dict):
    data = load(io.StringIO(yaml_string), Loader=LinkedLoader)
    assert data == docker_compose_dict


def test_linked_loader_renders_custom_yaml(
    mocker, minimal_yaml_string, linked_yaml_string
):
    def create_context():
        buf = io.StringIO()
        buf.write(minimal_yaml_string)
        mock_context = mock.MagicMock()
        mock_context.__enter__.return_value = buf
        mock_context.__exit__.return_value = False
        buf.seek(0)
        return mock_context

    mocker.patch(
        "builtins.open", return_value=create_context(), auto_spec=True, create=True
    )

    mocker.patch(
        "lnkd.loader.LinkedTag.fetch",
        return_value=create_context(),
        auto_spec=True,
        create=True,
    )

    data = load(io.StringIO(linked_yaml_string), Loader=LinkedLoader)

    assert data["services"]["client"]["build"]["name"] == "foxtrot"
    assert data["services"]["server"]["build"]["name"] == "foxtrot"


def test_linked_dumper_renders_custom_yaml():

    target_1 = """surplus:
  resource: !@ 'path/to/other.yaml'
test: !@ 'path/to/target.yaml'
"""

    data = {
        "test": LinkedTag("path/to/target.yaml"),
        "surplus": {"resource": LinkedTag("path/to/other.yaml")},
    }

    buf = io.StringIO()
    dump(data, buf, Dumper=LinkedDumper)

    assert buf.getvalue() == target_1
