/* wot-extractor: JavaScript FORMATADO a partir de sources/res/comp7/gui/gameface/_dist/production/mono/lobby/chunks/schedule_subheading.js. So foram alterados espacos e quebras de linha (verificado token a token e pelo node --check). NAO e o codigo-fonte original: o webpack/minificador encurtou nomes e removeu comentarios. */
import{
  r as s
}
from"./rolldown-runtime.js";
import{
  Ar as e,Cs as a,Mr as t,Na as o,Pr as n,Ts as r,cs as i,kr as m,ls as d,us as l
}
from"./lib.js";
import{
  a as c,i as x
}
from"./vendor.js";
import{
  n as p
}
from"./schedule_model.js";
import{
  t as g
}
from"./get_season_name.js";
import{
  t as j
}
from"./use_server_time_polling.js";
a();
var f=s=>{
  const e=Math.floor(s);
  return{
    totalSecondsLeft:e,seconds:Math.floor(e%60),minutes:Math.floor(e/60)%60,hours:Math.floor(e/3600%24),totalDays:Math.floor(e/86400)
  }
},
h=s(o()),u=(s,e,a=r.ShortDate)=>({
  startDate:(0,h.jsx)(n,{
    datetime:s,format:a
  }),endDate:(0,h.jsx)(n,{
    datetime:e,format:a
  })
}),_=(s,e,a)=>{
  const o=e-a,n=((s,e)=>f(s-e))(e,a);
  return o>=604800?(0,h.jsx)(t,{
    text:`${R.strings.comp7_ext.season.range()}`,binding:u(s,e)
  }):o>=86400?(0,h.jsx)(t,{
    text:R.strings.comp7_ext.season.daysLeft(),binding:n
  }):o>=3600?(0,h.jsx)(t,{
    text:R.strings.comp7_ext.season.hoursLeft(),binding:n
  }):o>=60?(0,h.jsx)(t,{
    text:R.strings.comp7_ext.season.minutesLeft(),binding:n
  }):o>=1?(0,h.jsx)(t,{
    text:R.strings.comp7_ext.season.secondsLeft(),binding:n
  }):void 0
},
v=s(x()),N="ActiveSeasonState_7be3b725",S="ActiveSeasonState_calendarIcon_59b8982c",b="ActiveSeasonState_divider_82fcaca5",T=({
  startTimestamp:s,endTimestamp:a,currentTimestamp:t,seasonName:o,tooltipId:n="",hasSeasonName:r=!0,classNames:i
})=>(0,h.jsx)(e,{
  args:{
    tooltipId:n
  },
  isEnabled:Boolean(n),children:(0,h.jsxs)("div",{
    className:N,children:[(0,h.jsx)("div",{
      className:(0,v.default)(S,i?.calendarIcon)
    }),r&&(0,h.jsxs)(h.Fragment,{
      children:[g(o),(0,h.jsx)("div",{
        className:b
      })]
    }),_(s,a,t)]
  })
}),I="ScheduleSubheading_6a634a68",M=c(({
  className:s,classNames:e,hasSeasonName:a=!0
})=>{
  const{
    model:t,controls:o
  }=p(),n=t.season.startTimestamp.get(),r=t.season.endTimestamp.get(),i=t.season.serverTimestamp.get(),d=t.season.name.get();
  return j(i,r,o.pollServerTime),(0,h.jsx)("div",{
    className:(0,v.default)(I,s),children:i<r?(0,h.jsx)("div",{
      className:e?.activeSeasonState,children:(0,h.jsx)(T,{
        startTimestamp:n,endTimestamp:r,currentTimestamp:i,seasonName:d,tooltipId:t.root.get().tooltipId,hasSeasonName:a,classNames:e?.scheduleClassNames
      })
    }):(0,h.jsx)(m,{
      text:R.strings.comp7_ext.season.over(),binding:{
        seasonName:g(d)
      }
    })
  })
});
export{
  u as n,M as t
};