/*------------------------------------
 *Author:FortunaTheme
 *Template:Rivo
 *Version:1.1
 *-------------------------------------
 */
(function ($) {

  "use strict";

  jQuery(document).on("ready", function () {



    /*
     * -----------------------------------------------------------------
     *---------------------------Preloader and Anchor Tag---------------
     * -----------------------------------------------------------------
     */

    var themeWindow = $(window);
    var pagebody = $('html, body');
    themeWindow.on("load", function () {

      var preloader = jQuery('.preloader');
      var preloaderArea = jQuery('.preloader-area');
      preloader.fadeOut();
      preloaderArea.delay(200).fadeOut('slow');
      themeWindow.scrollTop(0);
    });

    var anchor = $('a[href="#"]');
    anchor.on("click", function () {
      e.preventDefault();
    });


    /*
     * -----------------------------------------------------------------
     *-------------------single-page-nav-plugin------------------------
     * -----------------------------------------------------------------
     */



    // Prevent console.log from generating errors in IE for the purposes of the demo
    if (!window.console) console = {
      log: function () { }
    };

    // The actual plugin
    if ($(".welcome-area").is("#welcome-area")) {
      var singleNav = jQuery('.single-page-nav');
      singleNav.singlePageNav({
        offset: singleNav.outerHeight(),
        filter: ':not(.external)',
        updateHash: false
      });

      /*
       * -----------------------------------------------------------------
       *-------------------------Skill------------------------------------
       * -----------------------------------------------------------------
       */

      var skill = $('.about');

      var width1 = $(".prog1").data("progress");
      var progBar1 = $(".prog1");
      skill.waypoint(function () {
        progBar1.css({
          "width": width1,
          "transition": "2s ease-in"
        });
      }, {

        offset: width1
      });


      var width2 = $(".prog2").data("progress");
      var progBar2 = $(".prog2");
      skill.waypoint(function () {
        progBar2.css({
          "width": width2,
          "transition": "2s ease-in"
        });
      }, {

        offset: width2
      });


      var width3 = $(".prog3").data("progress");
      var progBar3 = $(".prog3");
      skill.waypoint(function () {
        progBar3.css({
          "width": width3,
          "transition": "2s ease-in"
        });
      }, {

        offset: width3
      });



      /*
       * -----------------------------------------------------------------
       *-------------------------------Mixit Up---------------------------
       * -----------------------------------------------------------------
       */



      var portfolioContent = $('.portfolio-content');

      portfolioContent.mixItUp();



      /*
       * -----------------------------------------------------------------
       *-----------------------------lightbox-----------------------------
       * -----------------------------------------------------------------
       */



      lightbox.option({
        'resizeDuration': 200,
        'wrapAround': true,
        showImageNumberLabel: false,
      });


      /*
       * -----------------------------------------------------------------
       *-----------------------------Ajax Chimp---------------------------
       * -----------------------------------------------------------------
       */


      var chimpForm = $('#mc-form');

      chimpForm.ajaxChimp({
        url: 'https://tahsinscreation.us17.list-manage.com/subscribe/post?u=8d43c37bb4dbc0d0b8078d874&amp;id=c638bf1e04'
      });




      /*
       * -----------------------------------------------------------------
       *----------------------Contact form ajax---------------------------
       * -----------------------------------------------------------------
       */



      var contactSubmit = $('#contact-submit');

      contactSubmit.on('click', function (e) {
        e.preventDefault();
        var name = $('#form-name').val();
        var email = $('#form-email').val();
        var subject = $('#form-subject').val();
        var message = $('#form-message').val();
        var form = new Array({
          'name': name,
          'email': email,
          'subject': subject,
          'message': message
        });
        $.ajax({
          type: 'POST',
          url: "contact.php",
          data: ({
            'action': 'contact',
            'form': form
          })
        }).done(function (data) {

          var conResult = $('#contact .result');
          conResult.html(data);
          $(".contact-form-area")[0].reset();

        });

      });


      /*
       * -----------------------------------------------------------------
       *--------------------Owl Carousel For Testimonial------------------
       * -----------------------------------------------------------------
       */



      var testimonial = $("#client-testimonial #owl-demo-testimonial");

      testimonial.owlCarousel({
        autoplay: true,
        autoplayTimeout: 5000,
        items: 2,
        autoPlay: 6000,
        responsive: {
          // breakpoint from 0 up
          0: {
            items: 1
          },
          // breakpoint from 480 up
          600: {
            items: 1
          },
          // breakpoint from 768 up
          900: {
            items: 2
          },
          1000: {
            items: 3
          }
        },
        pauseOnHover: true,
        nav: true,
        dots: false,
        navText: ["<i class='fas fa-arrow-left'></i>", "<i class='fas fa-arrow-right'></i>"]
      });

      var blog = $("#blog #owl-demo-blog");

      blog.owlCarousel({
        autoplay: true,
        autoplayTimeout: 5000,
        items: 1,
        autoPlay: 6000,
        responsive: {
          // breakpoint from 0 up
          0: {
            items: 1
          },
          // breakpoint from 480 up
          600: {
            items: 1
          },
          // breakpoint from 768 up
          900: {
            items: 1
          },
          1000: {
            items: 1
          }
        },
        pauseOnHover: true,
        nav: true,
        dots: false,
        navText: ["<i class='fas fa-arrow-left'></i>", "<i class='fas fa-arrow-right'></i>"]
      });




      /*
       * -----------------------------------------------------------------
       *-----------------------------Typed Js-----------------------------
       * -----------------------------------------------------------------
       */

      if ($(".welcome-area").is(".animated-text")) {
        var typed = new Typed("#typed", {
          stringsElement: '#typed-strings',
          typeSpeed: 60,
          backSpeed: 30,
          backDelay: 2000,
          startDelay: 1000,
          loop: true

        });
      }

    }
    /*
     * -----------------------------------------------------------------
     *----------------------- Pagepiling.js------------------------------
     * -----------------------------------------------------------------
     */


    var pagepiling = $('#pagepiling');
    pagepiling.pagepiling({
      menu: '#mainMenu',
      direction: 'vertical',
      verticalCentered: true,
      sectionsColor: [],
      anchors: ['home', 'about', 'myskills', 'resume', 'portfolio', 'contact'],
      scrollingSpeed: 700,
      easing: 'swing',
      loopBottom: true,
      loopTop: true,
      css3: true,
      navigation: {
        'textColor': '#000',
        'bulletsColor': '#000',
        'position': 'right'
      },
      normalScrollElements: null,
      normalScrollElementTouchThreshold: 5,
      touchSensitivity: 5,
      keyboardScrolling: true,
      sectionSelector: '.section',
      animateAnchor: true,

      //events
      afterRender: function () { },
      afterLoad: function (anchorLink, index) { }
    });

    /*
     * -----------------------------------------------------------------
     *----------------------- header info bar---------------------------
     * -----------------------------------------------------------------
     */


    var headerInfo = $("#header-info-btn");

    headerInfo.animatedModal({
      modalTarget: 'header-info-bar',
      animatedIn: 'fadeInRight',
      animatedOut: 'fadeOutRight',
    });

    /*
     * -----------------------------------------------------------------
     *--------------------MagnificPopup---------------------------------
     * -----------------------------------------------------------------
     */



    var videoPlay = $('.video-play');
    videoPlay.magnificPopup({
      type: 'iframe',
      closeBtnInside: false,
      closeOnContentClick: true,
      tLoading: '', // remove text from preloader
    });

    /*
     * -----------------------------------------------------------------
     *-------------------------Vanta.js---------------------------------
     * -----------------------------------------------------------------
     */

    if ($(".vanta-bg").is(".bird")) {
      VANTA.BIRDS({
        el: "#welcome-vanta-area",
        backgroundColor: 0xc0baa6,
        color1: 0x0,
        color2: 0x0,
        colorMode: "lerp",
        wingSpan: 14.00,
        separation: 59.00,
        cohesion: 17.00,
        quantity: 3.00,
        backgroundAlpha: 0.00
      })

    }
    if ($(".vanta-bg").is(".fog")) {
      VANTA.FOG({
        el: "#welcome-vanta-area",
        highlightColor: 0x9ec8e6,
        midtoneColor: 0x979acf,
        baseColor: 0x141414,
        blurFactor: 0.61,
        speed: 2.60
      })
    }

    if ($(".vanta-bg").is(".waves")) {
      VANTA.WAVES({
        el: "#welcome-vanta-area",
        color: 0x19303e,
        zoom: 1.22
      })
    }

    if ($(".vanta-bg").is(".cloud")) {
      VANTA.CLOUDS({
        el: "#welcome-vanta-area",
        skyColor: 0x1a1d34,
        cloudColor: 0x5e697a,
        cloudShadowColor: 0xb1020
      })
    }

  });

})(jQuery);