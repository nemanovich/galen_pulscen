# Карточка товара в портальном поисковом листинге типа "список"

=======================================
product-item             css      .js-product
content-body             css      .pi-body
image                    css      .img-block
comparison-block         css      .pi-label
title                    css      .pi-title-wrapper
price                    css      .pi-price
availability             css      li.available
amount                   css      li.amount
content                  css      .js-bp-desc
actualized               css      .pi-actualized
create_order             css      .js-bpal-link-write-message
expand-company-info      css      .pi-button

company-info             css      .company-info
company_name             css      li.company
rank-row                 css      li.rank-row
company_region           css      li.region
phone                    css      .js-show-phone-number
add-to-bookmarks         css      .add-to-bookmarks
more_products            css      .js-bp-more-link
=======================================

@ Content | all
-------------------------------------
add-to-bookmarks
    on top right: parent ~38 px left, 1 px top

image
    inside: content-body 0 px top left
comparison-block
    below: image ~10 px
    aligned vertically left: image

title
    near: image ~20 px right
price
    below: title ~10 px
    aligned vertically left: title
availability
    below: price 8 px
    aligned vertically left: title
amount
    near: availability ~21 px right
content
    below: availability ~8 px
    aligned vertically left: title
create_order
    below: content ~12 px
    aligned vertically left: title

@ Company info | desktop-XL, desktop-L
-------------------------------------
company-info
    near: title ~20 px right

@ ^ | desktop-M, tablet, mobile, company-info-collapsed
-------------------------------------
expand-company-info
    on bottom right: parent ~47 px top, ~40 px left
company-info
    absent

@ Company info expanded | desktop-M, tablet, mobile, company-info-expanded
-------------------------------------
company-info
    visible
    below: title
company_name
    visible