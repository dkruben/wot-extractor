/* wot-extractor: JavaScript FORMATADO a partir de sources/res/comp7/gui/gameface/_dist/production/mono/lobby/intro_screen/bundle.js. So foram alterados espacos e quebras de linha (verificado token a token e pelo node --check). NAO e o codigo-fonte original: o webpack/minificador encurtou nomes e removeu comentarios. */
import{
  r as e
}
from"../chunks/rolldown-runtime.js";
import{
  Cs as s,Dr as a,Er as n,Go as t,Hr as i,Io as r,Ma as o,Mr as c,Na as d,Qo as l,Rr as _,_i as u,ca as m,fi as h,io as p,na as g,ro as f,ta as b
}
from"../chunks/lib.js";
import"../chunks/_wg-global-styles.js";
import{
  a as x,i as S
}
from"../chunks/vendor.js";
/* empty css               */import{
  n as j,t as v
}
from"../chunks/schedule_model.js";
import{
  t as I
}
from"../chunks/get_button_size.js";
import{
  t as k
}
from"../chunks/schedule_subheading.js";
import{
  t as N
}
from"../chunks/use_server_time_polling.js";
import{
  t as w
}
from"../chunks/arrow_button.js";
import{
  t as D
}
from"../chunks/get_roman_levels.js";
var A=e(s(),1),[C,T]=u()(({
  observableModel:e
})=>({
  root:e.object(),vehicleLevels:e.array("vehicleLevels")
}),({
  externalModel:e
})=>({
  close:e.createCallbackNoArgs("onClose")
})),y=e(S(),1),L="CountDownSubheading_3410a94d",M="CountDownSubheading_highlight_8ca1da33",$="CountDownSubheading_timeLeftText_83a0f10d",z="CountDownSubheading_countDownContainer_95936a62",O="CountDownSubheading_countDownText_c438ad0f",W="CountDownSubheading_timer_dfa1cd55",E=e(d(),1),H=({
  timeLeft:e,className:s
})=>(0,E.jsx)("div",{
  className:(0,y.default)(L,s),children:(0,E.jsx)(c,{
    text:R.strings.comp7_ext.countDown.text(),binding:{
      timeLeft:(0,E.jsxs)("div",{
        className:z,children:[(0,E.jsx)("div",{
          className:M
        }),(0,E.jsx)("div",{
          className:W
        }),(0,E.jsx)(n,{
          duration:e,icon:a.None,classNames:{
            text:O
          }
        })]
      })
    },
    classMix:$
  })
}),U={
  countDown:"IntroSubheading_countDown_674b18af",fadeIn:"IntroSubheading_fadeIn_4ca45996",fadeInThreeQuarters:"IntroSubheading_fadeInThreeQuarters_4ca45996",fadeInHalf:"IntroSubheading_fadeInHalf_4ca45996",fadeOut:"IntroSubheading_fadeOut_4ca45996",fadeInWithScale:"IntroSubheading_fadeInWithScale_4ca45996",slideUp:"IntroSubheading_slideUp_4ca45996",scale:"IntroSubheading_scale_4ca45996",raysAppearance:"IntroSubheading_raysAppearance_4ca45996",rotate:"IntroSubheading_rotate_4ca45996","reverse-rotate":"IntroSubheading_reverse-rotate_4ca45996",glowAppearance:"IntroSubheading_glowAppearance_4ca45996",highlightAppearance:"IntroSubheading_highlightAppearance_4ca45996",blink:"IntroSubheading_blink_4ca45996",slideUpIn:"IntroSubheading_slideUpIn_4ca45996"
},
Q=x(()=>{
  const{
    model:e,controls:s
  }=j(),a=e.season.startTimestamp.get(),n=e.season.endTimestamp.get(),t=e.season.serverTimestamp.get();
  return N(t,n,s.pollServerTime),(0,E.jsx)("div",{
    className:U.base,children:t<a?(0,E.jsx)(H,{
      timeLeft:a-t,className:U.countDown
    }):(0,E.jsx)(k,{})
  })
}),q="Slide_680b9fee",B="Slide_title_442d6e94",G="Slide_icon_2921c32",F="Slide_description_a6104f8",P=x(({
  id:e
})=>{
  const{
    model:s
  }=T(),{
    model:a
  }=j(),{
    qualificationBattlesCount:n
  }=s.root.get(),t=`url(${"ranks"===e?R.images.comp7.gui.maps.icons.metaIntro.$dyn(`ranks_${a.season.name.get()}`):R.images.comp7.gui.maps.icons.metaIntro.$dyn(e)})`,i=D(s.vehicleLevels.get(),R.strings.comp7_ext.listSeparator());
  return(0,E.jsxs)("div",{
    className:q,children:[(0,E.jsx)(c,{
      text:String(R.strings.comp7_ext.intro.title.$dyn(e)),classMix:B
    }),(0,E.jsx)("div",{
      className:G,style:{
        backgroundImage:t
      }
    }),(0,E.jsx)(c,{
      text:`${R.strings.comp7_ext.intro.description.$plural(e,n)}`,binding:{
        count:n,levels:i
      },
      classMix:F
    })]
  })
}),J="Slider_caaf79d4",K="Slider_trackWrapper_9b67f47e",V="Slider_track_e521f890",X="Slider_track__withoutTransition_df13aef3",Y="Slider_slide_727efd4",Z="Slider_slide__active_b616c59f",ee="Slider_arrow_4c311c25",se="Slider_arrow__left_5cd6617d",ae="Slider_arrow__right_5676bbb7",ne="Slider_counter_8cf4b130",te="Slider_counterDivider_3d5ed95",ie=["vehiclesOnMap","banPhase","onslaughtModifiers","pointsOfInterest","roleSkills","draw","nightMaps","qualification","ranks"],re=ie.length,oe=(e,s)=>()=>{
  e||(s(),l.click(),l.sound(R.sounds.bp_glide_01()))
},
ce=({
  className:e
})=>{
  const[s,a]=(0,A.useState)(0),[n,t]=(0,A.useState)(!1),i=0===s,o=s===re-1;
  m(()=>{
    const e=()=>{
      t(!0)
    };
    return window.addEventListener("resize",e),()=>{
      window.removeEventListener("resize",e)
    }
  }),(0,A.useEffect)(()=>p(()=>f(()=>{
    n&&t(!1)
  },500)),[n]);
  const c=oe(i,()=>a(s-1)),d=oe(o,()=>a(s+1));
  return g(r.ARROW_LEFT,c),g(r.ARROW_RIGHT,d),(0,E.jsxs)("div",{
    className:(0,y.default)(J,e),style:{
      "--currentSlideIndex":s,"--transitionDuration":"500ms"
    },
    children:[(0,E.jsx)(w,{
      size:"medium",direction:"left",disabled:i,className:(0,y.default)(ee,se),onClick:c
    }),(0,E.jsx)(w,{
      size:"medium",direction:"right",disabled:o,className:(0,y.default)(ee,ae),onClick:d
    }),(0,E.jsxs)("div",{
      className:K,children:[(0,E.jsxs)("div",{
        className:ne,children:[s+1,(0,E.jsx)("div",{
          className:te,children:"/"
        }),re]
      }),(0,E.jsx)("div",{
        className:(0,y.default)(V,n&&X),children:ie.map((e,a)=>(0,E.jsx)("div",{
          className:(0,y.default)(Y,a===s&&Z),children:(0,E.jsx)(P,{
            id:e
          })
        },`slide-${a}`))
      })]
    })]
  })
},
de="App_33100033",le="App_content_24a8a318",_e="App_slider_87749c8a",ue="App_buttonWrapper_bc918676",me="App_button_b6edc495",he=x(function(){
  const{
    controls:e
  }=T(),{
    mediaSize:s
  }=o();
  return b(e.close),(0,E.jsxs)("div",{
    className:de,children:[(0,E.jsx)(Q,{}),(0,E.jsx)("div",{
      className:le,children:(0,E.jsx)(ce,{
        className:_e
      })
    }),(0,E.jsx)("div",{
      className:ue,children:(0,E.jsx)(_,{
        theme:_.themes.primary,size:I(s),className:me,onClick:e.close,children:R.strings.comp7_ext.intro.confirmButton()
      })
    })]
  })
});
t("comp7/gui/maps/icons/backgrounds/comp7_bg.dds"),h((0,E.jsx)(i,{
  children:(0,E.jsx)(C,{
    children:(0,E.jsx)(v,{
      options:{
        context:"model.scheduleInfo"
      },
      children:(0,E.jsx)(he,{})
    })
  })
}),{
  fullScreen:!0
});