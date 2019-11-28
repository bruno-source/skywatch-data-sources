import pytest


@pytest.fixture
def xml_data():
    xml = """
    <urlset>
    <url>
    <loc>https://www.skywatch.com/data</loc>
    <changefreq>daily</changefreq>
    <priority>0.75</priority>
    <lastmod>2019-06-07</lastmod>
    <image:image>
    <image:loc>
    https://fake.jpg
    </image:loc>
    <image:title>Sources</image:title>
    <image:caption>
    Sentinel-2 Provider: ESA / Resolution: 10m / Tech specs
    </image:caption>
    </image:image>
    <image:image>
    <image:loc>
    https://fake.jpg
    </image:loc>
    <image:title>Sources</image:title>
    <image:caption>
    SuperView-1 Provider: SpaceView / Resolution: 50cm / Tech specs
    </image:caption>
    </image:image>
    </url>
    </urlset>
      """.strip().replace('\n', ' ')
    return xml
