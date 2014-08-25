load("../pages/PortalCatalogPage.js");
load("init.js");

forAll(devices, function (device) {
    test("Chelyabinsk product listing page 'with images' type on " + device.deviceName + " screen", function () {
        var driver = createDriver("http://" + domain, device.size);
        var page = new PortalCatalogPage(driver);
        page.open("http://www.chel." + domain + "/price/010101-truba-besshovnaja?listing_style=list");
        page.waitForIt();

        checkLayout(driver,
            "spec/portal/catalog/product/listing_page.spec",
            ["all", device.deviceName],
            ["company-info-expanded", "without-images"]);

        //С развернутым блоком информации о компании в первом товаре
        page.expand_company_info(1);
        checkLayout(driver,
            "spec/portal/catalog/product/listing_page.spec",
            ["all", device.deviceName],
            ["company-info-collapsed", "without-images"]);
        driver.quit();
    });

    test("Chelyabinsk product listing page 'without images' type on " + device.deviceName + " screen", function () {
        var driver = createDriver("http://" + domain, device.size);
        var page = new PortalCatalogPage(driver);
        page.open("http://www.chel." + domain + "/price/010101-truba-besshovnaja?listing_style=without_images");
        page.waitForIt();

        logged("without images listing with collapsed company info", function () {
            checkLayout(driver,
            "spec/portal/catalog/product/listing_page.spec",
            ["all", device.deviceName],
            ["company-info-expanded", "list"]);
        });

        //С развернутым блоком информации о компании в первом товаре
        page.expand_company_info(1);
        logged("without images listing with expanded company info", function () {
            checkLayout(driver,
            "spec/portal/catalog/product/listing_page.spec",
            ["all", device.deviceName],
            ["company-info-collapsed", "list"]);
        });
        driver.quit();
    });
});

