from tethys_sdk.base import TethysAppBase, url_map_maker


class AllAboutAHartHenrichsen(TethysAppBase):
    """
    Tethys app class for Y.
    """

    name = 'Y'
    index = 'all_about_a_hart_henrichsen:home'
    icon = 'all_about_a_hart_henrichsen/images/icon.gif'
    package = 'all_about_a_hart_henrichsen'
    root_url = 'all-about-a-hart-henrichsen'
    color = '#ac6b53'
    description = 'This app explains where I came from where am I and Where will I go'
    tags = 'Me, great, Civil Engineering, 10/10, , Hart'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='all-about-a-hart-henrichsen',
                controller='all_about_a_hart_henrichsen.controllers.home'
            ),
        )

        return url_maps
