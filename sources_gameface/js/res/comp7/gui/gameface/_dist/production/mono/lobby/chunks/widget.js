/* wot-extractor: JavaScript FORMATADO a partir de sources/res/comp7/gui/gameface/_dist/production/mono/lobby/chunks/widget.js. So foram alterados espacos e quebras de linha (verificado token a token e pelo node --check). NAO e o codigo-fonte original: o webpack/minificador encurtou nomes e removeu comentarios. */
import{
  r as e
}
from"./rolldown-runtime.js";
import{
  Cs as s,Er as a,Es as t,Na as r,Or as n,Ti as o,Wa as i,_i as d,_s as l,ao as c,gs as _,hs as p,ms as m,n as f,ps as g,pt as u,so as h,t as b,vi as T,vs as v,xs as x
}
from"./lib.js";
import{
  a as N
}
from"./vendor.js";
var w=function(e){
  return e.News="news",e.ShopPromo="shopPromo",e.None="none",e
}({});
w.News,w.News,w.ShopPromo,Math.floor(Date.now()/1e3);
var y={
  getter:T({
    type:w.News,description:"Watch very interesting video, with very long, very very interesting and meaningful description!",isVideo:!0,image:"https://pie-webbrg-cdn-stg.wgcdn.co/dcont/fb/image/whats_new_475x230_2.png"
  }),controls:()=>h(c("onClick","onClose"))
},
[j,C]=d("TeaserModel")(({
  observableModel:e
})=>e.primitives(["type","postCounter","description","text","isVideo","finishTime","image"]),({
  externalModel:e
})=>({
  onClick:e.createCallbackNoArgs("onClick"),onClose:e.createCallbackNoArgs("onClose")
})),k=e(s(),1),W={
  imageWrapper:"Teaser_imageWrapper_901f1116",vignette:"Teaser_vignette_32737740",base:"Teaser_a2a96284",base__video:"Teaser_base__video_3d4fdb7e",contentWrapper:"Teaser_contentWrapper_b44f0d64",image:"Teaser_image_41628c29",base__newsType:"Teaser_base__newsType_3d4fdb7e",base__shopPromoType:"Teaser_base__shopPromoType_3d4fdb7e",title:"Teaser_title_f8c387e3",counter:"Teaser_counter_6afc9955",closeButton:"Teaser_closeButton_c46a88df",text:"Teaser_text_8e0a588c",bottomContent:"Teaser_bottomContent_eb7878d6",description:"Teaser_description_f7e0ddfc",extendedText:"Teaser_extendedText_286b5b73",countdown:"Teaser_countdown_40e45fc1",fadeIn:"Teaser_fadeIn_3d4fdb7e",fadeInThreeQuarters:"Teaser_fadeInThreeQuarters_3d4fdb7e",fadeInHalf:"Teaser_fadeInHalf_3d4fdb7e",fadeOut:"Teaser_fadeOut_3d4fdb7e",fadeInWithScale:"Teaser_fadeInWithScale_3d4fdb7e",slideUp:"Teaser_slideUp_3d4fdb7e",scale:"Teaser_scale_3d4fdb7e",raysAppearance:"Teaser_raysAppearance_3d4fdb7e",rotate:"Teaser_rotate_3d4fdb7e","reverse-rotate":"Teaser_reverse-rotate_3d4fdb7e",glowAppearance:"Teaser_glowAppearance_3d4fdb7e",highlightAppearance:"Teaser_highlightAppearance_3d4fdb7e",blink:"Teaser_blink_3d4fdb7e",slideUpIn:"Teaser_slideUpIn_3d4fdb7e"
},
I=e(r(),1),A="Teaser:Base",E=N(function({
  className:e,classNames:s
}){
  const{
    model:r,controls:d
  }=C(),c=r.type.get()||w.News,h=r.postCounter.get(),T=r.text.get(),N=r.description.get(),y=r.finishTime.get(),j=r.isVideo.get(),E=r.image.get(),M=o(),S=t.resolve("strings");
  const B=(0,k.useCallback)(e=>{
    e.stopPropagation(),d.onClose()
  },[d]),[P,O]=(0,k.useState)(null);
  (0,k.useLayoutEffect)(()=>{
    let e;
    const s=g(v(y||0),l());
    if(!y||s<=0)return void O(null);
    const a=Math.floor(p.seconds(s)),t=_(v(y),m(1))?n.Extended:n.Long;
    if(O({
      duration:a,style:t
    }),t===n.Extended){
      const s=g(v(a+1),m(1));
      e=setTimeout(()=>O(e=>({
        ...e,style:n.Long
      })),Math.min(s,i))
    }
    return()=>{
      e&&(clearTimeout(e),e=void 0)
    }
  },[y]);
  const[U,$]=(0,k.useState)(null),[L,V]=(0,k.useState)(!1);
  return(0,k.useEffect)(()=>{
    const e=new Image;
    return e.src=E,e.onload=()=>{
      $({
        path:E,height:e.height,width:e.width
      }),V(!0)
    },
    e.onerror=()=>{
      V(!0)
    },
    ()=>{
      e.src="",$(null)
    }
  },[E]),L?(0,I.jsxs)("div",{
    className:x(W.base,W[`base__${c}Type`],j&&W.base__video,e),onClick:function(e){
      M.play("click",{
        target:A,original:e
      }),d.onClick()
    },
    onMouseEnter:function(e){
      M.play("mouse-enter",{
        target:A,original:e
      })
    },
    children:[(0,I.jsx)("div",{
      className:x(W.contentWrapper,s?.contentWrapper),children:(0,I.jsx)("div",{
        className:x(W.imageWrapper,s?.imageWrapper),children:U&&(0,I.jsx)("div",{
          className:x(W.image,s?.image),style:{
            backgroundImage:`url(${U.path})`,height:`${U.height}rem`,width:`${U.width}rem`
          }
        })
      })
    }),(0,I.jsx)("div",{
      className:x(W.vignette,s?.vignette)
    }),(0,I.jsxs)("div",{
      className:x(W.contentWrapper,s?.contentWrapper),children:[(0,I.jsxs)("div",{
        className:x(W.title,s?.title),children:[S.readOrEmpty("menu.promo.teaser.title"),Boolean(h)&&h>0&&(0,I.jsx)(f,{
          className:x(W.counter,s?.counter),value:h,size:"small"
        })]
      }),(0,I.jsx)(b,{
        type:"close",side:"right",classNames:{
          base:x(W.closeButton,s?.closeButton)
        },
        onClick:B,caption:""
      }),T&&(0,I.jsx)("div",{
        className:x(W.text,s?.text),children:T
      }),(N||P)&&(0,I.jsxs)("div",{
        className:W.bottomContent,children:[N&&(0,I.jsx)("div",{
          className:x(W.description,s?.description),children:(0,I.jsx)(u,{
            classMix:W.extendedText,text:N,isTruncationAvailable:!0
          })
        }),P&&(0,I.jsx)(a,{
          className:x(W.countdown,s?.countdown),...P
        })]
      })]
    })]
  }):null
});
function M({
  className:e,classNames:s,...a
}){
  return(0,I.jsx)(j,{
    ...a,mode:"real",mocks:y,children:(0,I.jsx)(E,{
      className:e,classNames:s
    })
  })
}
export{
  M as default
};