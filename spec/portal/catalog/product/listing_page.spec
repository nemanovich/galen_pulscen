@@ import ../../../header.spec
@@ import traits_column.spec

=======================================
product-rubrics          css      .js-product-rubrics-list
facet-block              css      .facet-block
snippet                  css      p.snippet
viewed-rubrics           css      .js-viewed-rubrics

left-column              css      .col-left
right-column             css      .col-right
middle-column            css      .col-middle-background

products-list            id       products-list
product-*                css      li.js-product

add-product              css      a.js-add-product
right-adfox-banner       css      .adfox-banner-350 div#AF_kph2
vertical-showcases       id       vertical-showcases
vertical-showcase-*      css      #vertical-showcases div.sc
b2b-context              id       b2bcontext-goods-async
yandex-direct            xpath    //*[@id = 'yandex_ad_async']/preceding-sibling::*

#"Не нашли нужного предложения?"
communicate-block        css      .communicate-block
=======================================

@ Product portal listing | all
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

product-1
    component: spec/portal/catalog/product/list/product_card.spec

@ Product portal listing with vertical showcases | desktop-XL
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

@ ^ | desktop-L, tablet, mobile
-------------------------------------
add-product
    below: b2b-context ~15 px
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

yandex-direct
    below: communicate-block ~20 px
    aligned vertically all: middle-column