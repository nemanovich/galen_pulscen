load("../pages/PortalCatalogPage.js");

devices = {
    mobile: {
        deviceName: "mobile",
        size: "400x700"
    },
    tablet: {
        deviceName: "tablet",
        size: "600x800"
    },
    desktop_medium: {
        deviceName: "desktop-M",
        size: "1024x768"
    },
    desktop_large: {
        deviceName: "desktop-L",
        size: "1366x768"
    },
    desktop_extra_large: {
        deviceName: "desktop-XL",
        size: "1980x1024"
    }
};

forAll(devices, function (device) {
    test("Home page test on " + device.deviceName + " screen", function () {
        var driver = createDriver("http://test-pulscen.ru", device.size);

        var page = new PortalCatalogPage(driver);
        page.open("http://www.test-pulscen.ru/price/010101-truba-besshovnaja");
        page.waitForIt();

        checkLayout(driver, "spec/portal_product_listing_page.spec", ["all", device.deviceName]);
        driver.quit();
    });
});

afterTest(function (test) {
    var driver = session.get("driver");
    if (driver != null) {
        driver.quit();
    }
});
