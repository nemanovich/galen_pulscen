this.PortalCatalogPage = function (driver) {
    GalenPages.extendPage(this, driver, {
            right_adfox_banner: ".adfox-banner-350 div",
            vertical_showcases: "#vertical-showcases"}, {

            expand_company_info: function (index) {
                expand_company_info_link = this.findChildren(".pi-button")[index-1];
                if (expand_company_info_link.isDisplayed()) {
                    expand_company_info_link.click();
                }
            }
        }
    );
};