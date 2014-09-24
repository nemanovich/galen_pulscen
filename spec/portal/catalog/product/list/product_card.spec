# Карточка товара в портальном поисковом листинге "с фото, список"

=======================================
add-to-bookmarks         css      .add-to-bookmarks

product-content          css      .pi-body
image                    css      .img-block
comparison-block         css      .pi-label
title                    css      .pi-title-wrapper
price                    css      .pi-price
availability             css      li.available
amount                   css      li.amount
description              css      .js-bp-desc
actualized               css      .pi-actualized
create-order             css      .js-bpal-link-write-message
expand-company-info      css      .pi-button

company-info             css      .company-info
company-name             css      li.company
rank-row                 css      .rank-row
company-region           css      li.region
phone                    css      .js-show-phone-number
more-products            css      .js-bp-more-link
=======================================

@ Product content | all, list
-------------------------------------
image
    inside: product-content 0 px top left
title
    near: image ~20 px right
comparison-block
    below: image ~10 px
    aligned vertically left: image    

@ ^ | all, without-images
-------------------------------------
image
    absent
title
    inside: product-content 0 px top left
comparison-block
    near: create-order ~10 px right

@ ^ | all
-------------------------------------
add-to-bookmarks
    on top right: parent ~38 px left, ~1 px top
price
    below: title ~10 px
    aligned vertically left: title
availability
    below: price ~8 px
    aligned vertically left: title
amount
    near: availability ~21 px right
description
    below: availability ~8 px
    aligned vertically left: title
create-order
    below: description ~12 px
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
--------------------------------