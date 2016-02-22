/**
 * Created by Administrator on 2016/2/19.
 */
$(document).ready(function () {
    $('#nav-man').bind("mouseover", function () {
        $("#nav-man-contents").show(100);
    }).bind("mouseleave", function () {
        $("#nav-man-contents").hide();
    });
    $('#nav-woman').bind("mouseover", function () {
        $("#nav-woman-contents").show(100);
    }).bind("mouseleave", function () {
        $("#nav-woman-contents").hide();
    });


        $('#nav-man-contents').bind("mouseover", function () {
        $("#nav-man-contents").show();
    }).bind("mouseleave", function () {
        $("#nav-man-contents").hide(100);
    });
        $('#nav-woman-contents').bind("mouseover", function () {
        $("#nav-woman-contents").show();
    }).bind("mouseleave", function () {
        $("#nav-woman-contents").hide(100);
    });
});
