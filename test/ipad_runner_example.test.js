load("pages/PortalCatalogPage.js");

test("Home page test on mobile device", function () {
    var driver = createGridDriver("http://neman:4b1b8697-b3c9-41a1-b9d9-20c7877351ac@ondemand.saucelabs.com:80/wd/hub", {
        browser: "ipad",
        desiredCapabilities: {
            platform: "OS X 10.9",
            version: "7.1",
            deviceName: "iPad Simulator",
            "device-orientation": "landscape"
        }
    });

    var page = new PortalCatalogPage(driver);
    page.open("http://www.test-pulscen.ru/price/010101-truba-besshovnaja");
    page.waitForIt();

    checkLayout(driver, "spec/adaptive_portal_listing_page.spec", ["all"]);
});