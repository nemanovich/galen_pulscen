# Пагинатор. Только для большого количества страниц.

=======================================
pagination               css      .b-pagination-wrapper
prev-page                css      .b-pagination_headItemPrevious
next-page                css      .b-pagination_headItemNext
page-link-*              css      .b-pagination-listItem
pagination-slider        css      .b-pagination-slider
=======================================

@ Pagination | all
--------------------------------------
prev-page
    inside: pagination ~96px left, ~0px top
next-page
    near: prev-page 15px right
page-link-1
    inside: pagination 0px left
#Крайняя правая ссылка на таком расстоянии, чтобы не влезла следующая страница
page-link-${count("page-link-*")}
    inside: pagination < 43px right

[2 - ${count("page-link-*")}]
page-link-@
    below: prev-page ~10px
    near: page-link-@{-1} 0px right
    width: 43px
    height: 28px

pagination-slider
    below: page-link-1 ~0px
