# Хлебные крошки

=======================================
breadcrumbs-slider-visible     css      .breadcrumbs-slider-wrapper
breadcrumbs-slider             css      .breadcrumbs-slider
breadcrumb-link-*                    css      .bsi-link
arrow-prev                     xpath     //*[@data-dir='prev']
arrow-next                     xpath     //*[@data-dir='next']
=======================================

@ Breadcrumbs | all
-------------------------------------
@@ if
breadcrumbs-slider
    width: > 100% of breadcrumbs-slider-visible/width
@@ do
arrow-prev
    inside: breadcrumbs-slider-visible 0px top left
@@ otherwise
arrow-prev
    absent
breadcrumb-link-1
    inside: breadcrumbs-slider-visible 0px left
@@ end

[${count("breadcrumb-link-*")-1} - ${count("breadcrumb-link-*")}]
breadcrumb-link-@
    aligned horizontally all: breadcrumb-link-@{-1}
    near: breadcrumb-link-@{-1} ~24px right
