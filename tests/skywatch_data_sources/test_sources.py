import responses

from skywatch_data_sources.sources import get_data_sources


@responses.activate
def test_get_data_sources_success(xml_data):
    responses.add(
        responses.GET,
        'https://www.skywatch.com/sitemap.xml',
        body=xml_data,
        status=200
    )

    data_sources = get_data_sources()

    expected_result = [
        {
            'Source': 'Sentinel-2',
            'Provider': 'ESA',
            'Resolution': '10m'
        },
        {
            'Source': 'SuperView-1',
            'Provider': 'SpaceView',
            'Resolution': '50cm'
        }
    ]

    assert data_sources == expected_result
    assert len(responses.calls) == 1


@responses.activate
def test_get_data_sources_error(xml_data):
    responses.add(
        responses.GET,
        'https://www.skywatch.com/sitemap.xml',
        body='{error}$ 541',
        status=404
    )

    data_sources = get_data_sources()

    expected_result = []

    assert data_sources == expected_result
    assert len(responses.calls) == 1
