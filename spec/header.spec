# Портальный хидер (поисковая строка)

=======================================
header                   css      .js-phw-wrapper
header-logo              css      .portal-logo
search-block             css      .search-block
choose-region-link       css      .choose-region-link
=======================================

@ Header | all
--------------------------------------
search-block:
    near: header-logo ~33px right

@ ^ | desktop-XL, desktop-L
--------------------------------------
choose-region-link:
    near: search-block ~33px right

@ ^ | desktop-M, tablet
------------------------
header
    width: ~100% of screen/width
header-logo  
    inside: header 3 px left
choose-region-link:
    absent

