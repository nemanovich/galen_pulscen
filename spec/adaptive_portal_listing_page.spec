=======================================
header                   css      header
header-logo              css      .portal-logo
search-block             css      .search-block
choose-region-link       css      .choose-region-link

left-column              css      .col-left
right-column             css      .col-right
middle-column            css      .col-middle

products-list            id       products-list
product-*                css      li.js-product

add-product              css      a.js-add-product
right-adfox-banner       css      .adfox-banner-350
vertical-showcases       id       vertical-showcases
vertical-showcase-*      css      #vertical-showcases div.sc
b2b-context              id       b2bcontext-goods-async
yandex-ad                xpath    //*[@id = 'yandex_ad_async']/preceding-sibling::*
=======================================

@ Header | all
--------------------------------------
search-block:
    near: header-logo 30px right
choose-region-link:
    near: search-block 30px right

@ Header | desktop-M
------------------------
header
    inside: viewport 0 px left
header-logo  
    inside: header 3 px left

@ Content | all
--------------------------------------
left-column
    width: 240px
    near: middle-column 0 px left
right-column
    width: 220px
add-product
    width: 220px
right-adfox-banner
    height: 350px
    aligned vertically all: add-product
    below: add-product ~21px
    near: products-list ~42 px right
b2b-context
    below: vertical-showcases ~21px
    aligned vertically all: right-adfox-banner
yandex-ad
    below: b2b-context ~15px
    aligned vertically all: b2b-context

@@ if
vertical-showcases
    visible
@@ do
vertical-showcases
    below: right-adfox-banner ~21px
    aligned vertically all: right-adfox-banner
@@ end

@ Products | all
------------------------
product-1
    visible
    component: spec/list_product_card_in_portal_listing.spec

# TODO: Витрин может и не быть, а if с темплейтами не работает. Вынести логику в отдельный .test
#[ 2 - ${count("vertical-showcase-*")} ]
#vertical-showcase-@
#     below: vertical-showcase-@{-1} ~20px
#     aligned vertically all: vertical-showcase-@{-1}
