load("../pages/PortalCatalogPage.js");

devices = {
    tablet: {
        deviceName: "tablet",
        size: "800x600"
    },
    desktop_medium: {
        deviceName: "desktop-M",
        size: "1024x768"
    },
    desktop_large: {
        deviceName: "desktop-L",
        size: "1200x768"
    },
    desktop_extra_large: {
        deviceName: "desktop-XL",
        size: "1366x768"
    }
    //  mobile: {
    //     deviceName: "mobile",
    //     size: "400x700"
    // },
};

forAll(devices, function (device) {
    test("Chelyabinsk product listing page on " + device.deviceName + " screen", function () {
        var driver = createDriver("http://test-pulscen.ru", device.size);

        var page = new PortalCatalogPage(driver);
        page.open("http://www.chel.test-pulscen.ru/price/010101-truba-besshovnaja");
        page.waitForIt();

        checkLayout(driver, "spec/portal/catalog/product/listing_page.spec", ["all", device.deviceName]);
        driver.quit();
    });
});

afterTest(function (test) {
    var driver = session.get("driver");
    if (driver != null) {
        driver.quit();
    }
});
