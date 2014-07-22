# Портальный хидер (поисковая строка)

=======================================
header                   css      header
header-logo              css      .portal-logo
search-block             css      .search-block
choose-region-link       css      .choose-region-link
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