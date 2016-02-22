/**
 * Created by Administrator on 2016/2/16.
 */
window.onload = function () {
select_sku($(':radio:first'))
};

function select_sku(e) {
    var num = $('#num');  //数量input
    var num_val = parseInt(num.val());  //数量里面的值
    var sku_num = parseInt($(e).attr('num'));  //选择的sku的库存
    var sku_price = $(e).attr('price');  //选择的sku的价格
    var price_text = $('#new_price');  //显示价格的元素
    var num_text = $('#num_text');  //显示库存的元素
    num_text.text(sku_num);
    price_text.text(sku_price);
    if (num_val > sku_num) {
        num.val(sku_num)
    }
}
function sub_num() {
    var num = $('#num');
    if (num.val() > 1) {
        num.val(num.val() - 1);
    }

}
function add_num() {
    var num = parseInt($('#num').val());
    var topnum = parseInt($(':radio:checked').attr('num'));
    //alert(topnum);
    if (num < topnum) {
        $('#num').val(1.0 + num);
    }
}