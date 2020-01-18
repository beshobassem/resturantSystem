$(function() {
    "use strict";
    $(window).on("scroll" , function() {
        var scrol = $(window).scrollTop();
        if(scrol >500) {
            $(".up").fadeIn();
        }
        else {
            $(".up").fadeOut();
        }

    /*$(".up").click(function() {

        $(window).scrollTop(0); //34an yro7 le pdait el saf7a
        });*/
    });

    $(".up").click(function() {
  $("html , body").animate({ scrollTop: 0 }, "slow");
  return false;
        });

});

$(function() {
    $('.h1').on('click' , function() {
    $(this).hide();
});
});

$(function() {
    $('#h2').on('click' , function() {
    $(this).hide();
});
});
$(function() {
    $(".s1").animate({top:"300px"} , 1300);
    });
$(function() {
    $(".s2").animate({top:"350px"} , 1000);
    });

$(function() {
    $(".s3").animate({top:"350px"} , 1500);
    });
$(function() {
    $(".s4").animate({top:"350px"} , 1500);
    });
$(function() {
    $(".s5").animate({top:"350px"} , 1800);
    });





















