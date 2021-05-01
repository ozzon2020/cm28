$(document).ready(function () {


    $('.ui.checkbox').checkbox();
  $('.ui.accordion').accordion()

  $('.toggle').click(function() {
    $('.ui.accordion').accordion('toggle', 1);
  });





    // show dropdown on hover
    //$('.ui.container  .ui.dropdown').dropdown({
        //on: 'hover'
    //});

  // hide and open menu on small screen
        //$('.ui.toggle.button').click(function() {
          //$('.ui.vertical.menu.mobmenu').toggle("250", "linear")
        
        //});


    /* Back to top fade */
    $(window).scroll(function (event) {
        var scroll = $(window).scrollTop();
        $('#toTop').hide();
        if (scroll > 300) {
            $('#toTop').show();
        } else {
            $('#toTop').hide();
        }

        if (scroll == 0) {
            $('#toTop').hide();
            $('.fixed.top.menu').removeClass('slide up');
        }
    });

 



    $('.ui .message .close').on('click', function() {
    $(this)
      .closest('.message')
      .transition('fade')
    ;
  })
;


        
            //$('.ui.sticky')
            //.sticky({
                //offset: 120,
                //bottomOffset: 1,
                //context: '#local_rightmenu'
            //})
            //;
            
    //$('.ui .menu.fb .item').tab();


    //$('.ui .menu.fb .item').on('click', function () {
        //$('.ui .menu.fb .item').removeClass('active');
        //$(this).addClass('active');
    //});
    
    //$('.masthead')
            //.visibility({
                //once: false,
                //onBottomPassed: function () {
                    //$('.fixed.menu.twopanel').transition('fade in');
                //},
                //onBottomPassedReverse: function () {
                    //$('.fixed.menu.twopanel').transition('fade out');
                //}
            //})
            //;
    //$('.special.cards .image').dimmer({
        //on: 'hover'
    //});



    //$('.menu  .browse')
            //.popup({
                //inline: true,
                //hoverable: true,
                //position: 'bottom center',
                //delay: {
                    //show: 300,
                    //hide: 800
                //}
            //})
            //;
    //// show dropdown on hover
    //$('.main.menu  .ui.dropdown').dropdown({
        //on: 'hover',
        //clearable: true
    //});
    
    $('.ui.checkbox').checkbox();


    //// lazy load images
    //$('.image').visibility({
        //type: 'image',
        //transition: 'vertical flip in',
        //duration: 500
    //});    
    
          //$('.main').visibility({
        //type: 'fixed',
        //offset: 0
      //});
      // create sidebar and attach to menu open
      //$('.ui.sidebar')
        //.sidebar('attach events', '.toc.item')
      //;
      //$('.main.mymenu.menu  .ui.dropdown').dropdown({
        //on: 'hover'
      //});
$('.ui.rating')
  .rating({
    //initialRating: 2,
    maxRating: 5
  })
;      
   $('.ui.rating')
  .rating('disable')
;   

//$('.ui.sticky')
  //.sticky({
    //context: '#example1'
  //})
//;
$('.infinite.example .demo.segment')
  .visibility({
    once: false,
    // update size when new content loads
    observeChanges: true,
    // load content on bottom edge visible
    onBottomVisible: function() {
      // loads a max of 5 times
      window.loadFakeContent();
    }
  })
;
//$('.demo.segment')
  //.visibility({
    //onTopVisible: function(calculations) {
      //// top is on screen
    //},
    //onTopPassed: function(calculations) {
      //// top of element passed
    //},
    //onUpdate: function(calculations) {
      //// do something whenever calculations adjust
      //updateTable(calculations);
    //}
  //})
//;
    //
    //$('.ui.rating')
  //.rating({
    //initialRating: 3,
    //maxRating: 5
  //})
 //;      
        
//$('.ui.simple.dropdown.item.floated.right') 
     //.dropdown({
        //clearable: true
      //})
    //;


    ////$('.ui.dropdown.my_')
      ////.dropdown({
        ////clearable: true
      ////})
    ////;
    
    //$('.ui.modal')
  //.modal()
//;
//$('#btnModal').click(function() {
 //$('.overlay.fullscreen.modal')
//.modal('show')
//;
//})

//$('#btn1').click(function() {
//$('.modal').modal('setting', {
    //onShow : function () {
        //$(this).css({
            //'margin' : '1px',
            //'position' : 'fixed',
            //'top' : '0',
            //'bottom' : '0',
            //'left' : '0',
            //'right' : '0',
            //'width' : 'auto'
        //});
    //}
  //}).modal('show'); 
//})


//$(function(){
        //$("#test").click(function(){
//$('.test').modal('setting', {
    //onShow : function () {
        //$(this).css({
            //'margin' : '1px',
            //'position' : 'fixed',
            //'top' : '0',
            //'bottom' : '0',
            //'left' : '0',
            //'right' : '0',
            //'width' : 'auto'
        //});
    //}
  //}).modal('show'); 
//})
        //$(".test").modal({
                //closable: true
        //});
//});


        $(".ui.toggle.button").click(function() {
          $(".mobile.only.grid .ui.vertical.menu").toggle(100);
        });

        $('.ui.scrolling.dropdown.item').dropdown({
                        clearable: true,
                        on: 'hover',
                        action: 'combo',
                        placeholder: 'any',
                        allowAdditions: true
                        });

        $('.title.my').on('click', function (){
          $(this).remove();	
        });
        
        //$(".ui.dropdown").dropdown();
        $('.ui.dropdown').dropdown({
                        });

        $('.title.my').on('click', function (){
          $(this).remove();	
        });
        
        $('.menu .item')
          .tab()
        ;
        
       
    
  $('.ui.reply.form.qs')
  .form({
    inline : true,
    on: 'blur',

    fields: {
      var: {
        identifier  : 'var',
        rules: [
          {
            type   : 'empty',
            prompt : 'Тема обязательна'
          }
        ]
      },
      theme: {
        identifier  : 'theme',
        rules: [
          {
            type   : 'minLength[3]',
            prompt : 'Тема вопроса обязательна'
          }
        ]
      },      
     name: {
        identifier  : 'name',
        rules: [
          {
            type   : 'minLength[3]',
            prompt : 'Имя обязательно от 3 символов'
          }
        ]
      },  
    email: {
        identifier  : 'email',
        rules: [
          {
            type   : 'email',
            prompt : 'Обязательно email'
          }, 
          {
            type: 'regExp',
            value: "^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$",
            prompt: 'Правильно укажите e-mail'
            }
        ]
      },
    main : {
        identifier  : 'main',
        rules: [
          {
            type   : 'minLength[15]',
            prompt : 'Вопрос должен состоять из минимум 15 символов'
          }
        ]
      }
    }    
  })
;

  $('.ui.form.order')
  .form({
    inline : true,
    on: 'blur',

    fields: {
    first_name: {
        identifier  : 'first_name',
        rules: [
          {
            type   : 'empty',
            prompt : 'Имя обязательно'
          }
        ]
      },
    last_name: {
        identifier  : 'last_name',
        rules: [
          {
            type   : 'minLength[2]',
            prompt : 'Фамилия обязательна от 2 символов'
          }
        ]
      },  
    postal_code: {
        identifier  : 'postal_code',
        rules: [
          {
            type   : 'regExp[/^[0-9]{6,6}$/]',
            prompt : 'Почтовый индекс 6 цифр'
          }
        ]
      },
    city: {
        identifier  : 'city',
        rules: [
          {
            type   :  'minLength[2]',
            prompt : 'Обязательно '
          }
        ]
      }, 
    address: {
        identifier  : 'address',
        rules: [
          {
            type   : 'minLength[15]',
            prompt : 'Адрес доставки от 15  символов'
          }
        ]
      },
    email: {
        identifier  : 'email',
        rules: [
          {
            type   : 'email',
            prompt : 'Адрес e-mail'
          }, 
          {
            type: 'regExp',
            value: "^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$",
            prompt: 'Правильно укажите e-mail'
            }
        ]
      },      
    phone: {
        identifier  : 'phone',
        rules: [
          {
            type   : 'regExp[/^[0-9_-]{7,20}$/]',
            prompt : 'Телефон для связи от 7 до 20 цифр'
          }
        ]
      },      
    payment : {
        identifier  : 'payment',
        rules: [
          {
            type   : 'empty',
            prompt : 'Способ платежа'
          }
        ]
      }
    }
  })
;

  $('.ui.reply.form.review')
  .form({
    inline : true,
    on: 'blur',

    fields: {
      rating: {
        identifier  : 'rating',
        rules: [
          {
            type   : 'empty',
            prompt : 'Выбрать'
          }
        ]
      },
     name: {
        identifier  : 'name',
        rules: [
          {
            type   : 'minLength[3]',
            prompt : 'Имя обязательно от 3 символов'
          }
        ]
      },  
    email: {
        identifier  : 'email',
        rules: [
          {
            type   : 'email',
            prompt : 'Обязательно email'
          }, 
          {
            type: 'regExp',
            value: "^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$",
            prompt: 'Правильно укажите e-mail'
            }
        ]
      },
    body : {
        identifier  : 'body ',
        rules: [
          {
            type   :'minLength[5]',
            prompt : 'Отзыв должен состоять из минимум 5 символов'
          }
        ]
      }
    }
  })
;
$('.button_id').on('click',function(){
     $('.form_id').submit();
 });

$('.button_id2').on('click',function(){
     $('.form_id2').submit();
 });
 
$('.special.cards .image').dimmer({
  on: 'hover',
  
});
$('.special.cards .image')
  .transition({
    animation : 'pulse',
    reverse   : false,
    interval  : 200
  })
; 

});

function sendMail(a, b) {
	location.href = 'm'+'a'+'i'+'l'+'t'+'o'+':'+a+'@'+b;
}

