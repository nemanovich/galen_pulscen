# Карточка товара в портальном поисковом листинге типа "список"

=======================================
add-to-bookmarks         css      .add-to-bookmarks

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
company-name             css      li.company
rank-row                 css      .rank-row
company-region           css      li.region
phone                    css      .js-show-phone-number
more-products            css      .js-bp-more-link
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

# Описание колонки поставщика
@ Company info | desktop-XL, desktop-L
-------------------------------------
company-info
    near: title ~20 px right
company-name
    aligned horizontally top: title
rank-row
    below: company-name ~11 px
    aligned vertically left: company-name
company-region
    below: rank-row ~11 px
    aligned vertically left: company-name
phone
    below: company-region ~11 px
    aligned vertically left: company-name
more-products
    below: phone ~11 px
    aligned vertically left: company-name

@ ^ | desktop-M, tablet, mobile, company-info-collapsed
-------------------------------------
expand-company-info
    on bottom right: parent ~47 px top, ~40 px left
company-info
    absent

@ Company info expanded | desktop-M, tablet, mobile, company-info-expanded
-------------------------------------
company-info
    below: title
company-name
    aligned vertically left: title
rank-row
    below: company-name ~11 px
    aligned vertically left: company-name
company-region
    below: rank-row ~11 px
    aligned vertically left: company-name
phone
    below: company-region ~11 px
    aligned vertically left: company-name
more-products
    below: phone ~11 px
    aligned vertically left: company-name