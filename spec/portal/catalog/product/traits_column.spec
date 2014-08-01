#TODO: сделать проверку просмотренных рубрик

=======================================
header-logo              css      .portal-logo
column-header            css      .col-header

product-rubrics          css      .js-product-rubrics-list
product_rubric_num-*     css      .js-product-rubrics-list.prl-item-opened.prl-num

blocks-devider-*         css      hr.blocks-devider

facet-header             css      b.tl-header
facet-block-*            css      .facet-block
# фасеты в обоих блоках - служебном и нет
facet-item-*             css      .facet

snippet                  css      p.snippet
viewed-rubrics           css      .js-viewed-rubrics
b2b-context              id       b2bcontext-goods-async
=======================================

@ Traits column | all
--------------------------------------
column-header
    aligned vertically left: header-logo

product-rubrics
    below: column-header ~25 px
    aligned vertically left: column-header
product_rubric_num-*
     inside: product-rubrics 0 px right

blocks-devider-1
    below: product-rubrics ~20 px
    above: facet-header ~20 px
    aligned vertically all: product-rubrics

facet-header
    aligned vertically left: product-rubrics
facet-block-1
    below: facet-header ~5 px
facet-item-*
    aligned vertically left: product-rubrics

# Блок с не служебными фасетами
@@ if
facet-block-2
    visible
@@ do
facet-block-2
    below: facet-block-1 ~15 px
    above: blocks-devider-2 ~20 px
@@ otherwise
blocks-devider-2
    below: facet-block-1 ~20 px
@@ end

blocks-devider-2
    above: snippet ~20 px
    aligned vertically all: product-rubrics

snippet
    aligned vertically all: product-rubrics

blocks-devider-3
    below: snippet ~20 px
    aligned vertically all: product-rubrics

region_firms_link
    below: blocks-devider-3 ~20 px