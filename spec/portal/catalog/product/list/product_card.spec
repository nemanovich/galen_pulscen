# Карточка товара в портальном поисковом листинге типа "список"

=======================================
content-body             css      .pi-body
#image
title                    css      .pi-title-wrapper
price                    css      .pi-price
availability             css      li.available
amount                   css      li.amount
content                  css      .js-bp-desc

#create_order
#compare
#chat_button
#actualized
company-info             css      .company-info
#company_name
#company_region
#phone
#add_to_bookmarks
#other_products
#medal
=======================================

@ Content | all
-------------------------------------
title
    visible
price
    below: title ~10 px
    aligned vertically left: title
availability
    below: price 8 px
    aligned vertically left: title
amount
    near: availability ~21 px right
content
    below: availability 8 px
    aligned vertically left: title

@ Company info | desktop-XL, desktop-L
-------------------------------------
company-info
    near: title ~20 px right

@ Company info | tablet, mobile
-------------------------------------
company-info
    absent