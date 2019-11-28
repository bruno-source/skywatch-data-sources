from unittest import mock

from skywatch_data_sources.cli import list_data_sources


@mock.patch('skywatch_data_sources.cli.get_data_sources', autospec=True)
def test_list_data_sources_success(mock_get_data_sources, cli_runner):
    data = {'Source': 'Sentinel-42', 'Provider': 'ESA', 'Resolution': '10m'}
    mock_get_data_sources.return_value = [data]

    result = cli_runner.invoke(list_data_sources)

    assert mock_get_data_sources.call_count == 1
    assert result.exit_code == 0
    assert data['Source'] in result.output


@mock.patch('skywatch_data_sources.cli.get_data_sources', autospec=True)
def test_list_data_sources_empty_list(mock_get_data_sources, cli_runner):
    mock_get_data_sources.return_value = []

    result = cli_runner.invoke(list_data_sources)

    expected_output = 'Could not retrieve data sources\n'

    assert mock_get_data_sources.call_count == 1
    assert result.exit_code == 0
    assert result.output == expected_output
