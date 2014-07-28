this.PortalCatalogPage = function (driver) {
    GalenPages.extendPage(this, driver, {
        right_adfox_banner: ".adfox-banner-350 div",
        vertical_showcases: "#vertical-showcases"
    });
};