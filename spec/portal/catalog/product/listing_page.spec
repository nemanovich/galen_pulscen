@@ import ../../../header.spec
@@ import ../../../breadcrumbs.spec
@@ import ../../../pagination.spec
@@ import traits_column.spec

=======================================
adfox-banner-top         css      .adfox-banner-top

product-rubrics          css      .js-product-rubrics-list
facet-block              css      .facet-block
snippet                  css      p.snippet
viewed-rubrics           css      .js-viewed-rubrics
region_firms_link        css      .link-to-firms-from-predl

left-column              css      .col-left
right-column             css      .col-right
middle-column            css      .col-middle-background

breadcrumbs              css      .breadcrumbs-slider-wrapper
products-list            id       products-list
product-*                css      li.js-product
horizontal-showcases     css      .js-horizontal-showcases

add-product              css      a.js-add-product
right-adfox-banner       css      .adfox-banner-350 div#AF_kph2
vertical-showcases       id       vertical-showcases
vertical-showcase-*      css      #vertical-showcases div.sc
blocks-devider-*         css      hr.blocks-devider
b2b-context              id       b2bcontext-goods-async
yandex-direct            xpath    //*[@id = 'yandex_ad_async']/preceding-sibling::*

#"Не нашли нужного предложения?"
communicate-block        css      .communicate-block
=======================================

@ Product portal listing with vertical showcases | all
-------------------------------------
add-product
    width: 220px

@@ if
right-adfox-banner
    visible
@@ do
right-adfox-banner
    aligned vertically all: add-product
    height: 350 to 360 px
    below: add-product ~21px
@@ end

breadcrumbs
    below: adfox-banner-top ~106px
    above: middle-column ~31px
    aligned vertically left: middle-column
    inside: screen ~3px right
product-1
    component: spec/portal/catalog/product/list/product_card.spec
horizontal-showcases
    below: product-2 ~0 px
    aligned vertically all: product-2

@ ^ | desktop-XL
-------------------------------------
add-product
    near: products-list ~42 px right
vertical-showcases
    aligned vertically all: add-product

@@ if
right-adfox-banner
    visible
@@ do
right-adfox-banner
    aligned vertically all: add-product
    below: add-product ~21px
vertical-showcases
    below: right-adfox-banner 10 to 20 px
@@ otherwise
vertical-showcases
    below: add-product ~20 px
@@ end

yandex-direct
    below: vertical-showcases ~20 px
    aligned vertically all: vertical-showcases

b2b-context
    below: region_firms_link ~20 px
    aligned vertically all: product-rubrics

@ ^ | desktop-L, desktop-M, tablet, mobile
-------------------------------------
add-product
    below: region_firms_link ~20 px
    near: products-list ~42 px left
vertical-showcases
    aligned vertically all: add-product

@@ if
right-adfox-banner
   visible
@@ do
right-adfox-banner
    near: products-list ~42 px left
    aligned vertically all: add-product
vertical-showcases
    below: right-adfox-banner 10 to 20 px
@@ otherwise
vertical-showcases
    below: add-product 10 to 20 px
@@ end

b2b-context
    below: vertical-showcases ~20 px

yandex-direct
    below: communicate-block ~20 px
    aligned vertically all: middle-column