import{m as L,n as l,p as Ze,s as eo,q as oo,v as ze,x as oe,y as u,z as P,r as F,A as pe,B as Q,c as f,C as fe,D as Z,E as c,F as k,N as Ae,G,H as le,I as ee,J as to,K as J,L as ue,M as ro,O as no,P as lo,Q as ke,R as io,S as ao,d as j,h as S,o as E,a as so,u as co,U as uo,V as vo,W as mo,j as Ie,w as X,f as U,g as ho,X as po,e as W,Y as Se,k as _e,t as ae,T as fo}from"./index-Zmiy9vUZ.js";import{b as go,a as bo}from"./barbara-logo-light-kThTxLms.js";import{_ as xo}from"./_plugin-vue_export-helper-DlAUqK2U.js";import{S as Ne,u as Oe,V as Co}from"./Scrollbar-CDqUNXMD.js";import{u as yo,N as D}from"./Icon-mzXUnXfI.js";import{P as wo}from"./PeopleOutline-aKbrOAhK.js";import{P as zo}from"./PulseOutline-V2jb8RYn.js";import{C as ko}from"./CalendarOutline-BhKeG2Nz.js";import{C as Io,N as So}from"./Dropdown-Dw2a3L2M.js";import{f as se,c as $,k as ge}from"./browser-BZH80bmF.js";import{u as ve}from"./use-merged-state-BdofJKEv.js";import{N as _o}from"./Tooltip-_zUDYhM6.js";import{k as ce}from"./fade-in-scale-up.cssr-DeT7XIyr.js";import{c as de,V as Ro}from"./Popover-DQZh3cob.js";import{B as Po}from"./Button-DKNg9UAj.js";import"./get-C0N94DP8.js";const To=L({name:"ChevronDownFilled",render(){return l("svg",{viewBox:"0 0 16 16",fill:"none",xmlns:"http://www.w3.org/2000/svg"},l("path",{d:"M3.20041 5.73966C3.48226 5.43613 3.95681 5.41856 4.26034 5.70041L8 9.22652L11.7397 5.70041C12.0432 5.41856 12.5177 5.43613 12.7996 5.73966C13.0815 6.0432 13.0639 6.51775 12.7603 6.7996L8.51034 10.7996C8.22258 11.0668 7.77743 11.0668 7.48967 10.7996L3.23966 6.7996C2.93613 6.51775 2.91856 6.0432 3.20041 5.73966Z",fill:"currentColor"}))}});function Ao(e){const{baseColor:r,textColor2:o,bodyColor:a,cardColor:s,dividerColor:i,actionColor:d,scrollbarColor:x,scrollbarColorHover:m,invertedColor:b}=e;return{textColor:o,textColorInverted:"#FFF",color:a,colorEmbedded:d,headerColor:s,headerColorInverted:b,footerColor:d,footerColorInverted:b,headerBorderColor:i,headerBorderColorInverted:b,footerBorderColor:i,footerBorderColorInverted:b,siderBorderColor:i,siderBorderColorInverted:b,siderColor:s,siderColorInverted:b,siderToggleButtonBorder:`1px solid ${i}`,siderToggleButtonColor:r,siderToggleButtonIconColor:o,siderToggleButtonIconColorInverted:o,siderToggleBarColor:ze(a,x),siderToggleBarColorHover:ze(a,m),__invertScrollbar:"true"}}const Be=Ze({name:"Layout",common:oo,peers:{Scrollbar:eo},self:Ao}),He=oe("n-layout-sider"),Le={type:String,default:"static"},No=u("layout",`
 color: var(--n-text-color);
 background-color: var(--n-color);
 box-sizing: border-box;
 position: relative;
 z-index: auto;
 flex: auto;
 overflow: hidden;
 transition:
 box-shadow .3s var(--n-bezier),
 background-color .3s var(--n-bezier),
 color .3s var(--n-bezier);
`,[u("layout-scroll-container",`
 overflow-x: hidden;
 box-sizing: border-box;
 height: 100%;
 `),P("absolute-positioned",`
 position: absolute;
 left: 0;
 right: 0;
 top: 0;
 bottom: 0;
 `)]),Oo={embedded:Boolean,position:Le,nativeScrollbar:{type:Boolean,default:!0},scrollbarProps:Object,onScroll:Function,contentClass:String,contentStyle:{type:[String,Object],default:""},hasSider:Boolean,siderPlacement:{type:String,default:"left"}},Me=oe("n-layout");function Bo(e){return L({name:"Layout",props:Object.assign(Object.assign({},Q.props),Oo),setup(r){const o=F(null),a=F(null),{mergedClsPrefixRef:s,inlineThemeDisabled:i}=pe(r),d=Q("Layout","-layout",No,Be,r,s);function x(I,R){if(r.nativeScrollbar){const{value:A}=o;A&&(R===void 0?A.scrollTo(I):A.scrollTo(I,R))}else{const{value:A}=a;A&&A.scrollTo(I,R)}}Z(Me,r);let m=0,b=0;const _=I=>{var R;const A=I.target;m=A.scrollLeft,b=A.scrollTop,(R=r.onScroll)===null||R===void 0||R.call(r,I)};Oe(()=>{if(r.nativeScrollbar){const I=o.value;I&&(I.scrollTop=b,I.scrollLeft=m)}});const O={display:"flex",flexWrap:"nowrap",width:"100%",flexDirection:"row"},h={scrollTo:x},B=f(()=>{const{common:{cubicBezierEaseInOut:I},self:R}=d.value;return{"--n-bezier":I,"--n-color":r.embedded?R.colorEmbedded:R.color,"--n-text-color":R.textColor}}),T=i?fe("layout",f(()=>r.embedded?"e":""),B,r):void 0;return Object.assign({mergedClsPrefix:s,scrollableElRef:o,scrollbarInstRef:a,hasSiderStyle:O,mergedTheme:d,handleNativeElScroll:_,cssVars:i?void 0:B,themeClass:T==null?void 0:T.themeClass,onRender:T==null?void 0:T.onRender},h)},render(){var r;const{mergedClsPrefix:o,hasSider:a}=this;(r=this.onRender)===null||r===void 0||r.call(this);const s=a?this.hasSiderStyle:void 0,i=[this.themeClass,e,`${o}-layout`,`${o}-layout--${this.position}-positioned`];return l("div",{class:i,style:this.cssVars},this.nativeScrollbar?l("div",{ref:"scrollableElRef",class:[`${o}-layout-scroll-container`,this.contentClass],style:[this.contentStyle,s],onScroll:this.handleNativeElScroll},this.$slots):l(Ne,Object.assign({},this.scrollbarProps,{onScroll:this.onScroll,ref:"scrollbarInstRef",theme:this.mergedTheme.peers.Scrollbar,themeOverrides:this.mergedTheme.peerOverrides.Scrollbar,contentClass:this.contentClass,contentStyle:[this.contentStyle,s]}),this.$slots))}})}const Re=Bo(!1),Ho=u("layout-sider",`
 flex-shrink: 0;
 box-sizing: border-box;
 position: relative;
 z-index: 1;
 color: var(--n-text-color);
 transition:
 color .3s var(--n-bezier),
 border-color .3s var(--n-bezier),
 min-width .3s var(--n-bezier),
 max-width .3s var(--n-bezier),
 transform .3s var(--n-bezier),
 background-color .3s var(--n-bezier);
 background-color: var(--n-color);
 display: flex;
 justify-content: flex-end;
`,[P("bordered",[c("border",`
 content: "";
 position: absolute;
 top: 0;
 bottom: 0;
 width: 1px;
 background-color: var(--n-border-color);
 transition: background-color .3s var(--n-bezier);
 `)]),c("left-placement",[P("bordered",[c("border",`
 right: 0;
 `)])]),P("right-placement",`
 justify-content: flex-start;
 `,[P("bordered",[c("border",`
 left: 0;
 `)]),P("collapsed",[u("layout-toggle-button",[u("base-icon",`
 transform: rotate(180deg);
 `)]),u("layout-toggle-bar",[k("&:hover",[c("top",{transform:"rotate(-12deg) scale(1.15) translateY(-2px)"}),c("bottom",{transform:"rotate(12deg) scale(1.15) translateY(2px)"})])])]),u("layout-toggle-button",`
 left: 0;
 transform: translateX(-50%) translateY(-50%);
 `,[u("base-icon",`
 transform: rotate(0);
 `)]),u("layout-toggle-bar",`
 left: -28px;
 transform: rotate(180deg);
 `,[k("&:hover",[c("top",{transform:"rotate(12deg) scale(1.15) translateY(-2px)"}),c("bottom",{transform:"rotate(-12deg) scale(1.15) translateY(2px)"})])])]),P("collapsed",[u("layout-toggle-bar",[k("&:hover",[c("top",{transform:"rotate(-12deg) scale(1.15) translateY(-2px)"}),c("bottom",{transform:"rotate(12deg) scale(1.15) translateY(2px)"})])]),u("layout-toggle-button",[u("base-icon",`
 transform: rotate(0);
 `)])]),u("layout-toggle-button",`
 transition:
 color .3s var(--n-bezier),
 right .3s var(--n-bezier),
 left .3s var(--n-bezier),
 border-color .3s var(--n-bezier),
 background-color .3s var(--n-bezier);
 cursor: pointer;
 width: 24px;
 height: 24px;
 position: absolute;
 top: 50%;
 right: 0;
 border-radius: 50%;
 display: flex;
 align-items: center;
 justify-content: center;
 font-size: 18px;
 color: var(--n-toggle-button-icon-color);
 border: var(--n-toggle-button-border);
 background-color: var(--n-toggle-button-color);
 box-shadow: 0 2px 4px 0px rgba(0, 0, 0, .06);
 transform: translateX(50%) translateY(-50%);
 z-index: 1;
 `,[u("base-icon",`
 transition: transform .3s var(--n-bezier);
 transform: rotate(180deg);
 `)]),u("layout-toggle-bar",`
 cursor: pointer;
 height: 72px;
 width: 32px;
 position: absolute;
 top: calc(50% - 36px);
 right: -28px;
 `,[c("top, bottom",`
 position: absolute;
 width: 4px;
 border-radius: 2px;
 height: 38px;
 left: 14px;
 transition: 
 background-color .3s var(--n-bezier),
 transform .3s var(--n-bezier);
 `),c("bottom",`
 position: absolute;
 top: 34px;
 `),k("&:hover",[c("top",{transform:"rotate(12deg) scale(1.15) translateY(-2px)"}),c("bottom",{transform:"rotate(-12deg) scale(1.15) translateY(2px)"})]),c("top, bottom",{backgroundColor:"var(--n-toggle-bar-color)"}),k("&:hover",[c("top, bottom",{backgroundColor:"var(--n-toggle-bar-color-hover)"})])]),c("border",`
 position: absolute;
 top: 0;
 right: 0;
 bottom: 0;
 width: 1px;
 transition: background-color .3s var(--n-bezier);
 `),u("layout-sider-scroll-container",`
 flex-grow: 1;
 flex-shrink: 0;
 box-sizing: border-box;
 height: 100%;
 opacity: 0;
 transition: opacity .3s var(--n-bezier);
 max-width: 100%;
 `),P("show-content",[u("layout-sider-scroll-container",{opacity:1})]),P("absolute-positioned",`
 position: absolute;
 left: 0;
 top: 0;
 bottom: 0;
 `)]),Lo=L({props:{clsPrefix:{type:String,required:!0},onClick:Function},render(){const{clsPrefix:e}=this;return l("div",{onClick:this.onClick,class:`${e}-layout-toggle-bar`},l("div",{class:`${e}-layout-toggle-bar__top`}),l("div",{class:`${e}-layout-toggle-bar__bottom`}))}}),Mo=L({name:"LayoutToggleButton",props:{clsPrefix:{type:String,required:!0},onClick:Function},render(){const{clsPrefix:e}=this;return l("div",{class:`${e}-layout-toggle-button`,onClick:this.onClick},l(Ae,{clsPrefix:e},{default:()=>l(Io,null)}))}}),Eo={position:Le,bordered:Boolean,collapsedWidth:{type:Number,default:48},width:{type:[Number,String],default:272},contentClass:String,contentStyle:{type:[String,Object],default:""},collapseMode:{type:String,default:"transform"},collapsed:{type:Boolean,default:void 0},defaultCollapsed:Boolean,showCollapsedContent:{type:Boolean,default:!0},showTrigger:{type:[Boolean,String],default:!1},nativeScrollbar:{type:Boolean,default:!0},inverted:Boolean,scrollbarProps:Object,triggerClass:String,triggerStyle:[String,Object],collapsedTriggerClass:String,collapsedTriggerStyle:[String,Object],"onUpdate:collapsed":[Function,Array],onUpdateCollapsed:[Function,Array],onAfterEnter:Function,onAfterLeave:Function,onExpand:[Function,Array],onCollapse:[Function,Array],onScroll:Function},Fo=L({name:"LayoutSider",props:Object.assign(Object.assign({},Q.props),Eo),setup(e){const r=G(Me),o=F(null),a=F(null),s=F(e.defaultCollapsed),i=ve(le(e,"collapsed"),s),d=f(()=>se(i.value?e.collapsedWidth:e.width)),x=f(()=>e.collapseMode!=="transform"?{}:{minWidth:se(e.width)}),m=f(()=>r?r.siderPlacement:"left");function b(p,C){if(e.nativeScrollbar){const{value:y}=o;y&&(C===void 0?y.scrollTo(p):y.scrollTo(p,C))}else{const{value:y}=a;y&&y.scrollTo(p,C)}}function _(){const{"onUpdate:collapsed":p,onUpdateCollapsed:C,onExpand:y,onCollapse:H}=e,{value:V}=i;C&&$(C,!V),p&&$(p,!V),s.value=!V,V?y&&$(y):H&&$(H)}let O=0,h=0;const B=p=>{var C;const y=p.target;O=y.scrollLeft,h=y.scrollTop,(C=e.onScroll)===null||C===void 0||C.call(e,p)};Oe(()=>{if(e.nativeScrollbar){const p=o.value;p&&(p.scrollTop=h,p.scrollLeft=O)}}),Z(He,{collapsedRef:i,collapseModeRef:le(e,"collapseMode")});const{mergedClsPrefixRef:T,inlineThemeDisabled:I}=pe(e),R=Q("Layout","-layout-sider",Ho,Be,e,T);function A(p){var C,y;p.propertyName==="max-width"&&(i.value?(C=e.onAfterLeave)===null||C===void 0||C.call(e):(y=e.onAfterEnter)===null||y===void 0||y.call(e))}const q={scrollTo:b},K=f(()=>{const{common:{cubicBezierEaseInOut:p},self:C}=R.value,{siderToggleButtonColor:y,siderToggleButtonBorder:H,siderToggleBarColor:V,siderToggleBarColorHover:ie}=C,M={"--n-bezier":p,"--n-toggle-button-color":y,"--n-toggle-button-border":H,"--n-toggle-bar-color":V,"--n-toggle-bar-color-hover":ie};return e.inverted?(M["--n-color"]=C.siderColorInverted,M["--n-text-color"]=C.textColorInverted,M["--n-border-color"]=C.siderBorderColorInverted,M["--n-toggle-button-icon-color"]=C.siderToggleButtonIconColorInverted,M.__invertScrollbar=C.__invertScrollbar):(M["--n-color"]=C.siderColor,M["--n-text-color"]=C.textColor,M["--n-border-color"]=C.siderBorderColor,M["--n-toggle-button-icon-color"]=C.siderToggleButtonIconColor),M}),w=I?fe("layout-sider",f(()=>e.inverted?"a":"b"),K,e):void 0;return Object.assign({scrollableElRef:o,scrollbarInstRef:a,mergedClsPrefix:T,mergedTheme:R,styleMaxWidth:d,mergedCollapsed:i,scrollContainerStyle:x,siderPlacement:m,handleNativeElScroll:B,handleTransitionend:A,handleTriggerClick:_,inlineThemeDisabled:I,cssVars:K,themeClass:w==null?void 0:w.themeClass,onRender:w==null?void 0:w.onRender},q)},render(){var e;const{mergedClsPrefix:r,mergedCollapsed:o,showTrigger:a}=this;return(e=this.onRender)===null||e===void 0||e.call(this),l("aside",{class:[`${r}-layout-sider`,this.themeClass,`${r}-layout-sider--${this.position}-positioned`,`${r}-layout-sider--${this.siderPlacement}-placement`,this.bordered&&`${r}-layout-sider--bordered`,o&&`${r}-layout-sider--collapsed`,(!o||this.showCollapsedContent)&&`${r}-layout-sider--show-content`],onTransitionend:this.handleTransitionend,style:[this.inlineThemeDisabled?void 0:this.cssVars,{maxWidth:this.styleMaxWidth,width:se(this.width)}]},this.nativeScrollbar?l("div",{class:[`${r}-layout-sider-scroll-container`,this.contentClass],onScroll:this.handleNativeElScroll,style:[this.scrollContainerStyle,{overflow:"auto"},this.contentStyle],ref:"scrollableElRef"},this.$slots):l(Ne,Object.assign({},this.scrollbarProps,{onScroll:this.onScroll,ref:"scrollbarInstRef",style:this.scrollContainerStyle,contentStyle:this.contentStyle,contentClass:this.contentClass,theme:this.mergedTheme.peers.Scrollbar,themeOverrides:this.mergedTheme.peerOverrides.Scrollbar,builtinThemeOverrides:this.inverted&&this.cssVars.__invertScrollbar==="true"?{colorHover:"rgba(255, 255, 255, .4)",color:"rgba(255, 255, 255, .3)"}:void 0}),this.$slots),a?a==="bar"?l(Lo,{clsPrefix:r,class:o?this.collapsedTriggerClass:this.triggerClass,style:o?this.collapsedTriggerStyle:this.triggerStyle,onClick:this.handleTriggerClick}):l(Mo,{clsPrefix:r,class:o?this.collapsedTriggerClass:this.triggerClass,style:o?this.collapsedTriggerStyle:this.triggerStyle,onClick:this.handleTriggerClick}):null,this.bordered?l("div",{class:`${r}-layout-sider__border`}):null)}}),te=oe("n-menu"),Ee=oe("n-submenu"),be=oe("n-menu-item-group"),Pe=[k("&::before","background-color: var(--n-item-color-hover);"),c("arrow",`
 color: var(--n-arrow-color-hover);
 `),c("icon",`
 color: var(--n-item-icon-color-hover);
 `),u("menu-item-content-header",`
 color: var(--n-item-text-color-hover);
 `,[k("a",`
 color: var(--n-item-text-color-hover);
 `),c("extra",`
 color: var(--n-item-text-color-hover);
 `)])],Te=[c("icon",`
 color: var(--n-item-icon-color-hover-horizontal);
 `),u("menu-item-content-header",`
 color: var(--n-item-text-color-hover-horizontal);
 `,[k("a",`
 color: var(--n-item-text-color-hover-horizontal);
 `),c("extra",`
 color: var(--n-item-text-color-hover-horizontal);
 `)])],$o=k([u("menu",`
 background-color: var(--n-color);
 color: var(--n-item-text-color);
 overflow: hidden;
 transition: background-color .3s var(--n-bezier);
 box-sizing: border-box;
 font-size: var(--n-font-size);
 padding-bottom: 6px;
 `,[P("horizontal",`
 max-width: 100%;
 width: 100%;
 display: flex;
 overflow: hidden;
 padding-bottom: 0;
 `,[u("submenu","margin: 0;"),u("menu-item","margin: 0;"),u("menu-item-content",`
 padding: 0 20px;
 border-bottom: 2px solid #0000;
 `,[k("&::before","display: none;"),P("selected","border-bottom: 2px solid var(--n-border-color-horizontal)")]),u("menu-item-content",[P("selected",[c("icon","color: var(--n-item-icon-color-active-horizontal);"),u("menu-item-content-header",`
 color: var(--n-item-text-color-active-horizontal);
 `,[k("a","color: var(--n-item-text-color-active-horizontal);"),c("extra","color: var(--n-item-text-color-active-horizontal);")])]),P("child-active",`
 border-bottom: 2px solid var(--n-border-color-horizontal);
 `,[u("menu-item-content-header",`
 color: var(--n-item-text-color-child-active-horizontal);
 `,[k("a",`
 color: var(--n-item-text-color-child-active-horizontal);
 `),c("extra",`
 color: var(--n-item-text-color-child-active-horizontal);
 `)]),c("icon",`
 color: var(--n-item-icon-color-child-active-horizontal);
 `)]),ee("disabled",[ee("selected, child-active",[k("&:focus-within",Te)]),P("selected",[Y(null,[c("icon","color: var(--n-item-icon-color-active-hover-horizontal);"),u("menu-item-content-header",`
 color: var(--n-item-text-color-active-hover-horizontal);
 `,[k("a","color: var(--n-item-text-color-active-hover-horizontal);"),c("extra","color: var(--n-item-text-color-active-hover-horizontal);")])])]),P("child-active",[Y(null,[c("icon","color: var(--n-item-icon-color-child-active-hover-horizontal);"),u("menu-item-content-header",`
 color: var(--n-item-text-color-child-active-hover-horizontal);
 `,[k("a","color: var(--n-item-text-color-child-active-hover-horizontal);"),c("extra","color: var(--n-item-text-color-child-active-hover-horizontal);")])])]),Y("border-bottom: 2px solid var(--n-border-color-horizontal);",Te)]),u("menu-item-content-header",[k("a","color: var(--n-item-text-color-horizontal);")])])]),ee("responsive",[u("menu-item-content-header",`
 overflow: hidden;
 text-overflow: ellipsis;
 `)]),P("collapsed",[u("menu-item-content",[P("selected",[k("&::before",`
 background-color: var(--n-item-color-active-collapsed) !important;
 `)]),u("menu-item-content-header","opacity: 0;"),c("arrow","opacity: 0;"),c("icon","color: var(--n-item-icon-color-collapsed);")])]),u("menu-item",`
 height: var(--n-item-height);
 margin-top: 6px;
 position: relative;
 `),u("menu-item-content",`
 box-sizing: border-box;
 line-height: 1.75;
 height: 100%;
 display: grid;
 grid-template-areas: "icon content arrow";
 grid-template-columns: auto 1fr auto;
 align-items: center;
 cursor: pointer;
 position: relative;
 padding-right: 18px;
 transition:
 background-color .3s var(--n-bezier),
 padding-left .3s var(--n-bezier),
 border-color .3s var(--n-bezier);
 `,[k("> *","z-index: 1;"),k("&::before",`
 z-index: auto;
 content: "";
 background-color: #0000;
 position: absolute;
 left: 8px;
 right: 8px;
 top: 0;
 bottom: 0;
 pointer-events: none;
 border-radius: var(--n-border-radius);
 transition: background-color .3s var(--n-bezier);
 `),P("disabled",`
 opacity: .45;
 cursor: not-allowed;
 `),P("collapsed",[c("arrow","transform: rotate(0);")]),P("selected",[k("&::before","background-color: var(--n-item-color-active);"),c("arrow","color: var(--n-arrow-color-active);"),c("icon","color: var(--n-item-icon-color-active);"),u("menu-item-content-header",`
 color: var(--n-item-text-color-active);
 `,[k("a","color: var(--n-item-text-color-active);"),c("extra","color: var(--n-item-text-color-active);")])]),P("child-active",[u("menu-item-content-header",`
 color: var(--n-item-text-color-child-active);
 `,[k("a",`
 color: var(--n-item-text-color-child-active);
 `),c("extra",`
 color: var(--n-item-text-color-child-active);
 `)]),c("arrow",`
 color: var(--n-arrow-color-child-active);
 `),c("icon",`
 color: var(--n-item-icon-color-child-active);
 `)]),ee("disabled",[ee("selected, child-active",[k("&:focus-within",Pe)]),P("selected",[Y(null,[c("arrow","color: var(--n-arrow-color-active-hover);"),c("icon","color: var(--n-item-icon-color-active-hover);"),u("menu-item-content-header",`
 color: var(--n-item-text-color-active-hover);
 `,[k("a","color: var(--n-item-text-color-active-hover);"),c("extra","color: var(--n-item-text-color-active-hover);")])])]),P("child-active",[Y(null,[c("arrow","color: var(--n-arrow-color-child-active-hover);"),c("icon","color: var(--n-item-icon-color-child-active-hover);"),u("menu-item-content-header",`
 color: var(--n-item-text-color-child-active-hover);
 `,[k("a","color: var(--n-item-text-color-child-active-hover);"),c("extra","color: var(--n-item-text-color-child-active-hover);")])])]),P("selected",[Y(null,[k("&::before","background-color: var(--n-item-color-active-hover);")])]),Y(null,Pe)]),c("icon",`
 grid-area: icon;
 color: var(--n-item-icon-color);
 transition:
 color .3s var(--n-bezier),
 font-size .3s var(--n-bezier),
 margin-right .3s var(--n-bezier);
 box-sizing: content-box;
 display: inline-flex;
 align-items: center;
 justify-content: center;
 `),c("arrow",`
 grid-area: arrow;
 font-size: 16px;
 color: var(--n-arrow-color);
 transform: rotate(180deg);
 opacity: 1;
 transition:
 color .3s var(--n-bezier),
 transform 0.2s var(--n-bezier),
 opacity 0.2s var(--n-bezier);
 `),u("menu-item-content-header",`
 grid-area: content;
 transition:
 color .3s var(--n-bezier),
 opacity .3s var(--n-bezier);
 opacity: 1;
 white-space: nowrap;
 color: var(--n-item-text-color);
 `,[k("a",`
 outline: none;
 text-decoration: none;
 transition: color .3s var(--n-bezier);
 color: var(--n-item-text-color);
 `,[k("&::before",`
 content: "";
 position: absolute;
 left: 0;
 right: 0;
 top: 0;
 bottom: 0;
 `)]),c("extra",`
 font-size: .93em;
 color: var(--n-group-text-color);
 transition: color .3s var(--n-bezier);
 `)])]),u("submenu",`
 cursor: pointer;
 position: relative;
 margin-top: 6px;
 `,[u("menu-item-content",`
 height: var(--n-item-height);
 `),u("submenu-children",`
 overflow: hidden;
 padding: 0;
 `,[to({duration:".2s"})])]),u("menu-item-group",[u("menu-item-group-title",`
 margin-top: 6px;
 color: var(--n-group-text-color);
 cursor: default;
 font-size: .93em;
 height: 36px;
 display: flex;
 align-items: center;
 transition:
 padding-left .3s var(--n-bezier),
 color .3s var(--n-bezier);
 `)])]),u("menu-tooltip",[k("a",`
 color: inherit;
 text-decoration: none;
 `)]),u("menu-divider",`
 transition: background-color .3s var(--n-bezier);
 background-color: var(--n-divider-color);
 height: 1px;
 margin: 6px 18px;
 `)]);function Y(e,r){return[P("hover",e,r),k("&:hover",e,r)]}const Fe=L({name:"MenuOptionContent",props:{collapsed:Boolean,disabled:Boolean,title:[String,Function],icon:Function,extra:[String,Function],showArrow:Boolean,childActive:Boolean,hover:Boolean,paddingLeft:Number,selected:Boolean,maxIconSize:{type:Number,required:!0},activeIconSize:{type:Number,required:!0},iconMarginRight:{type:Number,required:!0},clsPrefix:{type:String,required:!0},onClick:Function,tmNode:{type:Object,required:!0},isEllipsisPlaceholder:Boolean},setup(e){const{props:r}=G(te);return{menuProps:r,style:f(()=>{const{paddingLeft:o}=e;return{paddingLeft:o&&`${o}px`}}),iconStyle:f(()=>{const{maxIconSize:o,activeIconSize:a,iconMarginRight:s}=e;return{width:`${o}px`,height:`${o}px`,fontSize:`${a}px`,marginRight:`${s}px`}})}},render(){const{clsPrefix:e,tmNode:r,menuProps:{renderIcon:o,renderLabel:a,renderExtra:s,expandIcon:i}}=this,d=o?o(r.rawNode):J(this.icon);return l("div",{onClick:x=>{var m;(m=this.onClick)===null||m===void 0||m.call(this,x)},role:"none",class:[`${e}-menu-item-content`,{[`${e}-menu-item-content--selected`]:this.selected,[`${e}-menu-item-content--collapsed`]:this.collapsed,[`${e}-menu-item-content--child-active`]:this.childActive,[`${e}-menu-item-content--disabled`]:this.disabled,[`${e}-menu-item-content--hover`]:this.hover}],style:this.style},d&&l("div",{class:`${e}-menu-item-content__icon`,style:this.iconStyle,role:"none"},[d]),l("div",{class:`${e}-menu-item-content-header`,role:"none"},this.isEllipsisPlaceholder?this.title:a?a(r.rawNode):J(this.title),this.extra||s?l("span",{class:`${e}-menu-item-content-header__extra`}," ",s?s(r.rawNode):J(this.extra)):null),this.showArrow?l(Ae,{ariaHidden:!0,class:`${e}-menu-item-content__arrow`,clsPrefix:e},{default:()=>i?i(r.rawNode):l(To,null)}):null)}}),ne=8;function xe(e){const r=G(te),{props:o,mergedCollapsedRef:a}=r,s=G(Ee,null),i=G(be,null),d=f(()=>o.mode==="horizontal"),x=f(()=>d.value?o.dropdownPlacement:"tmNodes"in e?"right-start":"right"),m=f(()=>{var h;return Math.max((h=o.collapsedIconSize)!==null&&h!==void 0?h:o.iconSize,o.iconSize)}),b=f(()=>{var h;return!d.value&&e.root&&a.value&&(h=o.collapsedIconSize)!==null&&h!==void 0?h:o.iconSize}),_=f(()=>{if(d.value)return;const{collapsedWidth:h,indent:B,rootIndent:T}=o,{root:I,isGroup:R}=e,A=T===void 0?B:T;return I?a.value?h/2-m.value/2:A:i&&typeof i.paddingLeftRef.value=="number"?B/2+i.paddingLeftRef.value:s&&typeof s.paddingLeftRef.value=="number"?(R?B/2:B)+s.paddingLeftRef.value:0}),O=f(()=>{const{collapsedWidth:h,indent:B,rootIndent:T}=o,{value:I}=m,{root:R}=e;return d.value||!R||!a.value?ne:(T===void 0?B:T)+I+ne-(h+I)/2});return{dropdownPlacement:x,activeIconSize:b,maxIconSize:m,paddingLeft:_,iconMarginRight:O,NMenu:r,NSubmenu:s,NMenuOptionGroup:i}}const Ce={internalKey:{type:[String,Number],required:!0},root:Boolean,isGroup:Boolean,level:{type:Number,required:!0},title:[String,Function],extra:[String,Function]},jo=L({name:"MenuDivider",setup(){const e=G(te),{mergedClsPrefixRef:r,isHorizontalRef:o}=e;return()=>o.value?null:l("div",{class:`${r.value}-menu-divider`})}}),$e=Object.assign(Object.assign({},Ce),{tmNode:{type:Object,required:!0},disabled:Boolean,icon:Function,onClick:Function}),Ko=ge($e),Vo=L({name:"MenuOption",props:$e,setup(e){const r=xe(e),{NSubmenu:o,NMenu:a,NMenuOptionGroup:s}=r,{props:i,mergedClsPrefixRef:d,mergedCollapsedRef:x}=a,m=o?o.mergedDisabledRef:s?s.mergedDisabledRef:{value:!1},b=f(()=>m.value||e.disabled);function _(h){const{onClick:B}=e;B&&B(h)}function O(h){b.value||(a.doSelect(e.internalKey,e.tmNode.rawNode),_(h))}return{mergedClsPrefix:d,dropdownPlacement:r.dropdownPlacement,paddingLeft:r.paddingLeft,iconMarginRight:r.iconMarginRight,maxIconSize:r.maxIconSize,activeIconSize:r.activeIconSize,mergedTheme:a.mergedThemeRef,menuProps:i,dropdownEnabled:ue(()=>e.root&&x.value&&i.mode!=="horizontal"&&!b.value),selected:ue(()=>a.mergedValueRef.value===e.internalKey),mergedDisabled:b,handleClick:O}},render(){const{mergedClsPrefix:e,mergedTheme:r,tmNode:o,menuProps:{renderLabel:a,nodeProps:s}}=this,i=s==null?void 0:s(o.rawNode);return l("div",Object.assign({},i,{role:"menuitem",class:[`${e}-menu-item`,i==null?void 0:i.class]}),l(_o,{theme:r.peers.Tooltip,themeOverrides:r.peerOverrides.Tooltip,trigger:"hover",placement:this.dropdownPlacement,disabled:!this.dropdownEnabled||this.title===void 0,internalExtraClass:["menu-tooltip"]},{default:()=>a?a(o.rawNode):J(this.title),trigger:()=>l(Fe,{tmNode:o,clsPrefix:e,paddingLeft:this.paddingLeft,iconMarginRight:this.iconMarginRight,maxIconSize:this.maxIconSize,activeIconSize:this.activeIconSize,selected:this.selected,title:this.title,extra:this.extra,disabled:this.mergedDisabled,icon:this.icon,onClick:this.handleClick})}))}}),je=Object.assign(Object.assign({},Ce),{tmNode:{type:Object,required:!0},tmNodes:{type:Array,required:!0}}),Do=ge(je),Uo=L({name:"MenuOptionGroup",props:je,setup(e){const r=xe(e),{NSubmenu:o}=r,a=f(()=>o!=null&&o.mergedDisabledRef.value?!0:e.tmNode.disabled);Z(be,{paddingLeftRef:r.paddingLeft,mergedDisabledRef:a});const{mergedClsPrefixRef:s,props:i}=G(te);return function(){const{value:d}=s,x=r.paddingLeft.value,{nodeProps:m}=i,b=m==null?void 0:m(e.tmNode.rawNode);return l("div",{class:`${d}-menu-item-group`,role:"group"},l("div",Object.assign({},b,{class:[`${d}-menu-item-group-title`,b==null?void 0:b.class],style:[(b==null?void 0:b.style)||"",x!==void 0?`padding-left: ${x}px;`:""]}),J(e.title),e.extra?l(ro,null," ",J(e.extra)):null),l("div",null,e.tmNodes.map(_=>ye(_,i))))}}});function me(e){return e.type==="divider"||e.type==="render"}function Go(e){return e.type==="divider"}function ye(e,r){const{rawNode:o}=e,{show:a}=o;if(a===!1)return null;if(me(o))return Go(o)?l(jo,Object.assign({key:e.key},o.props)):null;const{labelField:s}=r,{key:i,level:d,isGroup:x}=e,m=Object.assign(Object.assign({},o),{title:o.title||o[s],extra:o.titleExtra||o.extra,key:i,internalKey:i,level:d,root:d===0,isGroup:x});return e.children?e.isGroup?l(Uo,ce(m,Do,{tmNode:e,tmNodes:e.children,key:i})):l(he,ce(m,qo,{key:i,rawNodes:o[r.childrenField],tmNodes:e.children,tmNode:e})):l(Vo,ce(m,Ko,{key:i,tmNode:e}))}const Ke=Object.assign(Object.assign({},Ce),{rawNodes:{type:Array,default:()=>[]},tmNodes:{type:Array,default:()=>[]},tmNode:{type:Object,required:!0},disabled:Boolean,icon:Function,onClick:Function,domId:String,virtualChildActive:{type:Boolean,default:void 0},isEllipsisPlaceholder:Boolean}),qo=ge(Ke),he=L({name:"Submenu",props:Ke,setup(e){const r=xe(e),{NMenu:o,NSubmenu:a}=r,{props:s,mergedCollapsedRef:i,mergedThemeRef:d}=o,x=f(()=>{const{disabled:h}=e;return a!=null&&a.mergedDisabledRef.value||s.disabled?!0:h}),m=F(!1);Z(Ee,{paddingLeftRef:r.paddingLeft,mergedDisabledRef:x}),Z(be,null);function b(){const{onClick:h}=e;h&&h()}function _(){x.value||(i.value||o.toggleExpand(e.internalKey),b())}function O(h){m.value=h}return{menuProps:s,mergedTheme:d,doSelect:o.doSelect,inverted:o.invertedRef,isHorizontal:o.isHorizontalRef,mergedClsPrefix:o.mergedClsPrefixRef,maxIconSize:r.maxIconSize,activeIconSize:r.activeIconSize,iconMarginRight:r.iconMarginRight,dropdownPlacement:r.dropdownPlacement,dropdownShow:m,paddingLeft:r.paddingLeft,mergedDisabled:x,mergedValue:o.mergedValueRef,childActive:ue(()=>{var h;return(h=e.virtualChildActive)!==null&&h!==void 0?h:o.activePathRef.value.includes(e.internalKey)}),collapsed:f(()=>s.mode==="horizontal"?!1:i.value?!0:!o.mergedExpandedKeysRef.value.includes(e.internalKey)),dropdownEnabled:f(()=>!x.value&&(s.mode==="horizontal"||i.value)),handlePopoverShowChange:O,handleClick:_}},render(){var e;const{mergedClsPrefix:r,menuProps:{renderIcon:o,renderLabel:a}}=this,s=()=>{const{isHorizontal:d,paddingLeft:x,collapsed:m,mergedDisabled:b,maxIconSize:_,activeIconSize:O,title:h,childActive:B,icon:T,handleClick:I,menuProps:{nodeProps:R},dropdownShow:A,iconMarginRight:q,tmNode:K,mergedClsPrefix:w,isEllipsisPlaceholder:p,extra:C}=this,y=R==null?void 0:R(K.rawNode);return l("div",Object.assign({},y,{class:[`${w}-menu-item`,y==null?void 0:y.class],role:"menuitem"}),l(Fe,{tmNode:K,paddingLeft:x,collapsed:m,disabled:b,iconMarginRight:q,maxIconSize:_,activeIconSize:O,title:h,extra:C,showArrow:!d,childActive:B,clsPrefix:w,icon:T,hover:A,onClick:I,isEllipsisPlaceholder:p}))},i=()=>l(no,null,{default:()=>{const{tmNodes:d,collapsed:x}=this;return x?null:l("div",{class:`${r}-submenu-children`,role:"menu"},d.map(m=>ye(m,this.menuProps)))}});return this.root?l(So,Object.assign({size:"large",trigger:"hover"},(e=this.menuProps)===null||e===void 0?void 0:e.dropdownProps,{themeOverrides:this.mergedTheme.peerOverrides.Dropdown,theme:this.mergedTheme.peers.Dropdown,builtinThemeOverrides:{fontSizeLarge:"14px",optionIconSizeLarge:"18px"},value:this.mergedValue,disabled:!this.dropdownEnabled,placement:this.dropdownPlacement,keyField:this.menuProps.keyField,labelField:this.menuProps.labelField,childrenField:this.menuProps.childrenField,onUpdateShow:this.handlePopoverShowChange,options:this.rawNodes,onSelect:this.doSelect,inverted:this.inverted,renderIcon:o,renderLabel:a}),{default:()=>l("div",{class:`${r}-submenu`,role:"menu","aria-expanded":!this.collapsed,id:this.domId},s(),this.isHorizontal?null:i())}):l("div",{class:`${r}-submenu`,role:"menu","aria-expanded":!this.collapsed,id:this.domId},s(),i())}}),Wo=Object.assign(Object.assign({},Q.props),{options:{type:Array,default:()=>[]},collapsed:{type:Boolean,default:void 0},collapsedWidth:{type:Number,default:48},iconSize:{type:Number,default:20},collapsedIconSize:{type:Number,default:24},rootIndent:Number,indent:{type:Number,default:32},labelField:{type:String,default:"label"},keyField:{type:String,default:"key"},childrenField:{type:String,default:"children"},disabledField:{type:String,default:"disabled"},defaultExpandAll:Boolean,defaultExpandedKeys:Array,expandedKeys:Array,value:[String,Number],defaultValue:{type:[String,Number],default:null},mode:{type:String,default:"vertical"},watchProps:{type:Array,default:void 0},disabled:Boolean,show:{type:Boolean,default:!0},inverted:Boolean,"onUpdate:expandedKeys":[Function,Array],onUpdateExpandedKeys:[Function,Array],onUpdateValue:[Function,Array],"onUpdate:value":[Function,Array],expandIcon:Function,renderIcon:Function,renderLabel:Function,renderExtra:Function,dropdownProps:Object,accordion:Boolean,nodeProps:Function,dropdownPlacement:{type:String,default:"bottom"},responsive:Boolean,items:Array,onOpenNamesChange:[Function,Array],onSelect:[Function,Array],onExpandedNamesChange:[Function,Array],expandedNames:Array,defaultExpandedNames:Array}),Yo=L({name:"Menu",inheritAttrs:!1,props:Wo,setup(e){const{mergedClsPrefixRef:r,inlineThemeDisabled:o}=pe(e),a=Q("Menu","-menu",$o,lo,e,r),s=G(He,null),i=f(()=>{var v;const{collapsed:z}=e;if(z!==void 0)return z;if(s){const{collapseModeRef:t,collapsedRef:g}=s;if(t.value==="width")return(v=g.value)!==null&&v!==void 0?v:!1}return!1}),d=f(()=>{const{keyField:v,childrenField:z,disabledField:t}=e;return de(e.items||e.options,{getIgnored(g){return me(g)},getChildren(g){return g[z]},getDisabled(g){return g[t]},getKey(g){var N;return(N=g[v])!==null&&N!==void 0?N:g.name}})}),x=f(()=>new Set(d.value.treeNodes.map(v=>v.key))),{watchProps:m}=e,b=F(null);m!=null&&m.includes("defaultValue")?ke(()=>{b.value=e.defaultValue}):b.value=e.defaultValue;const _=le(e,"value"),O=ve(_,b),h=F([]),B=()=>{h.value=e.defaultExpandAll?d.value.getNonLeafKeys():e.defaultExpandedNames||e.defaultExpandedKeys||d.value.getPath(O.value,{includeSelf:!1}).keyPath};m!=null&&m.includes("defaultExpandedKeys")?ke(B):B();const T=yo(e,["expandedNames","expandedKeys"]),I=ve(T,h),R=f(()=>d.value.treeNodes),A=f(()=>d.value.getPath(O.value).keyPath);Z(te,{props:e,mergedCollapsedRef:i,mergedThemeRef:a,mergedValueRef:O,mergedExpandedKeysRef:I,activePathRef:A,mergedClsPrefixRef:r,isHorizontalRef:f(()=>e.mode==="horizontal"),invertedRef:le(e,"inverted"),doSelect:q,toggleExpand:w});function q(v,z){const{"onUpdate:value":t,onUpdateValue:g,onSelect:N}=e;g&&$(g,v,z),t&&$(t,v,z),N&&$(N,v,z),b.value=v}function K(v){const{"onUpdate:expandedKeys":z,onUpdateExpandedKeys:t,onExpandedNamesChange:g,onOpenNamesChange:N}=e;z&&$(z,v),t&&$(t,v),g&&$(g,v),N&&$(N,v),h.value=v}function w(v){const z=Array.from(I.value),t=z.findIndex(g=>g===v);if(~t)z.splice(t,1);else{if(e.accordion&&x.value.has(v)){const g=z.findIndex(N=>x.value.has(N));g>-1&&z.splice(g,1)}z.push(v)}K(z)}const p=v=>{const z=d.value.getPath(v??O.value,{includeSelf:!1}).keyPath;if(!z.length)return;const t=Array.from(I.value),g=new Set([...t,...z]);e.accordion&&x.value.forEach(N=>{g.has(N)&&!z.includes(N)&&g.delete(N)}),K(Array.from(g))},C=f(()=>{const{inverted:v}=e,{common:{cubicBezierEaseInOut:z},self:t}=a.value,{borderRadius:g,borderColorHorizontal:N,fontSize:Xe,itemHeight:Je,dividerColor:Qe}=t,n={"--n-divider-color":Qe,"--n-bezier":z,"--n-font-size":Xe,"--n-border-color-horizontal":N,"--n-border-radius":g,"--n-item-height":Je};return v?(n["--n-group-text-color"]=t.groupTextColorInverted,n["--n-color"]=t.colorInverted,n["--n-item-text-color"]=t.itemTextColorInverted,n["--n-item-text-color-hover"]=t.itemTextColorHoverInverted,n["--n-item-text-color-active"]=t.itemTextColorActiveInverted,n["--n-item-text-color-child-active"]=t.itemTextColorChildActiveInverted,n["--n-item-text-color-child-active-hover"]=t.itemTextColorChildActiveInverted,n["--n-item-text-color-active-hover"]=t.itemTextColorActiveHoverInverted,n["--n-item-icon-color"]=t.itemIconColorInverted,n["--n-item-icon-color-hover"]=t.itemIconColorHoverInverted,n["--n-item-icon-color-active"]=t.itemIconColorActiveInverted,n["--n-item-icon-color-active-hover"]=t.itemIconColorActiveHoverInverted,n["--n-item-icon-color-child-active"]=t.itemIconColorChildActiveInverted,n["--n-item-icon-color-child-active-hover"]=t.itemIconColorChildActiveHoverInverted,n["--n-item-icon-color-collapsed"]=t.itemIconColorCollapsedInverted,n["--n-item-text-color-horizontal"]=t.itemTextColorHorizontalInverted,n["--n-item-text-color-hover-horizontal"]=t.itemTextColorHoverHorizontalInverted,n["--n-item-text-color-active-horizontal"]=t.itemTextColorActiveHorizontalInverted,n["--n-item-text-color-child-active-horizontal"]=t.itemTextColorChildActiveHorizontalInverted,n["--n-item-text-color-child-active-hover-horizontal"]=t.itemTextColorChildActiveHoverHorizontalInverted,n["--n-item-text-color-active-hover-horizontal"]=t.itemTextColorActiveHoverHorizontalInverted,n["--n-item-icon-color-horizontal"]=t.itemIconColorHorizontalInverted,n["--n-item-icon-color-hover-horizontal"]=t.itemIconColorHoverHorizontalInverted,n["--n-item-icon-color-active-horizontal"]=t.itemIconColorActiveHorizontalInverted,n["--n-item-icon-color-active-hover-horizontal"]=t.itemIconColorActiveHoverHorizontalInverted,n["--n-item-icon-color-child-active-horizontal"]=t.itemIconColorChildActiveHorizontalInverted,n["--n-item-icon-color-child-active-hover-horizontal"]=t.itemIconColorChildActiveHoverHorizontalInverted,n["--n-arrow-color"]=t.arrowColorInverted,n["--n-arrow-color-hover"]=t.arrowColorHoverInverted,n["--n-arrow-color-active"]=t.arrowColorActiveInverted,n["--n-arrow-color-active-hover"]=t.arrowColorActiveHoverInverted,n["--n-arrow-color-child-active"]=t.arrowColorChildActiveInverted,n["--n-arrow-color-child-active-hover"]=t.arrowColorChildActiveHoverInverted,n["--n-item-color-hover"]=t.itemColorHoverInverted,n["--n-item-color-active"]=t.itemColorActiveInverted,n["--n-item-color-active-hover"]=t.itemColorActiveHoverInverted,n["--n-item-color-active-collapsed"]=t.itemColorActiveCollapsedInverted):(n["--n-group-text-color"]=t.groupTextColor,n["--n-color"]=t.color,n["--n-item-text-color"]=t.itemTextColor,n["--n-item-text-color-hover"]=t.itemTextColorHover,n["--n-item-text-color-active"]=t.itemTextColorActive,n["--n-item-text-color-child-active"]=t.itemTextColorChildActive,n["--n-item-text-color-child-active-hover"]=t.itemTextColorChildActiveHover,n["--n-item-text-color-active-hover"]=t.itemTextColorActiveHover,n["--n-item-icon-color"]=t.itemIconColor,n["--n-item-icon-color-hover"]=t.itemIconColorHover,n["--n-item-icon-color-active"]=t.itemIconColorActive,n["--n-item-icon-color-active-hover"]=t.itemIconColorActiveHover,n["--n-item-icon-color-child-active"]=t.itemIconColorChildActive,n["--n-item-icon-color-child-active-hover"]=t.itemIconColorChildActiveHover,n["--n-item-icon-color-collapsed"]=t.itemIconColorCollapsed,n["--n-item-text-color-horizontal"]=t.itemTextColorHorizontal,n["--n-item-text-color-hover-horizontal"]=t.itemTextColorHoverHorizontal,n["--n-item-text-color-active-horizontal"]=t.itemTextColorActiveHorizontal,n["--n-item-text-color-child-active-horizontal"]=t.itemTextColorChildActiveHorizontal,n["--n-item-text-color-child-active-hover-horizontal"]=t.itemTextColorChildActiveHoverHorizontal,n["--n-item-text-color-active-hover-horizontal"]=t.itemTextColorActiveHoverHorizontal,n["--n-item-icon-color-horizontal"]=t.itemIconColorHorizontal,n["--n-item-icon-color-hover-horizontal"]=t.itemIconColorHoverHorizontal,n["--n-item-icon-color-active-horizontal"]=t.itemIconColorActiveHorizontal,n["--n-item-icon-color-active-hover-horizontal"]=t.itemIconColorActiveHoverHorizontal,n["--n-item-icon-color-child-active-horizontal"]=t.itemIconColorChildActiveHorizontal,n["--n-item-icon-color-child-active-hover-horizontal"]=t.itemIconColorChildActiveHoverHorizontal,n["--n-arrow-color"]=t.arrowColor,n["--n-arrow-color-hover"]=t.arrowColorHover,n["--n-arrow-color-active"]=t.arrowColorActive,n["--n-arrow-color-active-hover"]=t.arrowColorActiveHover,n["--n-arrow-color-child-active"]=t.arrowColorChildActive,n["--n-arrow-color-child-active-hover"]=t.arrowColorChildActiveHover,n["--n-item-color-hover"]=t.itemColorHover,n["--n-item-color-active"]=t.itemColorActive,n["--n-item-color-active-hover"]=t.itemColorActiveHover,n["--n-item-color-active-collapsed"]=t.itemColorActiveCollapsed),n}),y=o?fe("menu",f(()=>e.inverted?"a":"b"),C,e):void 0,H=io(),V=F(null),ie=F(null);let M=!0;const we=()=>{var v;M?M=!1:(v=V.value)===null||v===void 0||v.sync({showAllItemsBeforeCalculate:!0})};function Ve(){return document.getElementById(H)}const re=F(-1);function De(v){re.value=e.options.length-v}function Ue(v){v||(re.value=-1)}const Ge=f(()=>{const v=re.value;return{children:v===-1?[]:e.options.slice(v)}}),qe=f(()=>{const{childrenField:v,disabledField:z,keyField:t}=e;return de([Ge.value],{getIgnored(g){return me(g)},getChildren(g){return g[v]},getDisabled(g){return g[z]},getKey(g){var N;return(N=g[t])!==null&&N!==void 0?N:g.name}})}),We=f(()=>de([{}]).treeNodes[0]);function Ye(){var v;if(re.value===-1)return l(he,{root:!0,level:0,key:"__ellpisisGroupPlaceholder__",internalKey:"__ellpisisGroupPlaceholder__",title:"···",tmNode:We.value,domId:H,isEllipsisPlaceholder:!0});const z=qe.value.treeNodes[0],t=A.value,g=!!(!((v=z.children)===null||v===void 0)&&v.some(N=>t.includes(N.key)));return l(he,{level:0,root:!0,key:"__ellpisisGroup__",internalKey:"__ellpisisGroup__",title:"···",virtualChildActive:g,tmNode:z,domId:H,rawNodes:z.rawNode.children||[],tmNodes:z.children||[],isEllipsisPlaceholder:!0})}return{mergedClsPrefix:r,controlledExpandedKeys:T,uncontrolledExpanededKeys:h,mergedExpandedKeys:I,uncontrolledValue:b,mergedValue:O,activePath:A,tmNodes:R,mergedTheme:a,mergedCollapsed:i,cssVars:o?void 0:C,themeClass:y==null?void 0:y.themeClass,overflowRef:V,counterRef:ie,updateCounter:()=>{},onResize:we,onUpdateOverflow:Ue,onUpdateCount:De,renderCounter:Ye,getCounter:Ve,onRender:y==null?void 0:y.onRender,showOption:p,deriveResponsiveState:we}},render(){const{mergedClsPrefix:e,mode:r,themeClass:o,onRender:a}=this;a==null||a();const s=()=>this.tmNodes.map(m=>ye(m,this.$props)),d=r==="horizontal"&&this.responsive,x=()=>l("div",ao(this.$attrs,{role:r==="horizontal"?"menubar":"menu",class:[`${e}-menu`,o,`${e}-menu--${r}`,d&&`${e}-menu--responsive`,this.mergedCollapsed&&`${e}-menu--collapsed`],style:this.cssVars}),d?l(Ro,{ref:"overflowRef",onUpdateOverflow:this.onUpdateOverflow,getCounter:this.getCounter,onUpdateCount:this.onUpdateCount,updateCounter:this.updateCounter,style:{width:"100%",display:"flex",overflow:"hidden"}},{default:s,counter:this.renderCounter}):s());return d?l(Co,{onResize:this.onResize},{default:x}):x()}}),Xo={xmlns:"http://www.w3.org/2000/svg","xmlns:xlink":"http://www.w3.org/1999/xlink",viewBox:"0 0 512 512"},Jo=L({name:"BriefcaseOutline",render:function(r,o){return E(),j("svg",Xo,o[0]||(o[0]=[S("rect",{x:"32",y:"128",width:"448",height:"320",rx:"48",ry:"48",fill:"none",stroke:"currentColor","stroke-linejoin":"round","stroke-width":"32"},null,-1),S("path",{d:"M144 128V96a32 32 0 0 1 32-32h160a32 32 0 0 1 32 32v32",fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"32"},null,-1),S("path",{fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"32",d:"M480 240H32"},null,-1),S("path",{d:"M320 240v24a8 8 0 0 1-8 8H200a8 8 0 0 1-8-8v-24",fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"32"},null,-1)]))}}),Qo={xmlns:"http://www.w3.org/2000/svg","xmlns:xlink":"http://www.w3.org/1999/xlink",viewBox:"0 0 512 512"},Zo=L({name:"FlaskOutline",render:function(r,o){return E(),j("svg",Qo,o[0]||(o[0]=[S("path",{fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-miterlimit":"10","stroke-width":"32",d:"M176 48h160"},null,-1),S("path",{fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-miterlimit":"10","stroke-width":"32",d:"M118 304h276"},null,-1),S("path",{d:"M208 48v93.48a64.09 64.09 0 0 1-9.88 34.18L73.21 373.49C48.4 412.78 76.63 464 123.08 464h265.84c46.45 0 74.68-51.22 49.87-90.51L313.87 175.66a64.09 64.09 0 0 1-9.87-34.18V48",fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-miterlimit":"10","stroke-width":"32"},null,-1)]))}}),et={xmlns:"http://www.w3.org/2000/svg","xmlns:xlink":"http://www.w3.org/1999/xlink",viewBox:"0 0 512 512"},ot=L({name:"GridOutline",render:function(r,o){return E(),j("svg",et,o[0]||(o[0]=[S("rect",{x:"48",y:"48",width:"176",height:"176",rx:"20",ry:"20",fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"32"},null,-1),S("rect",{x:"288",y:"48",width:"176",height:"176",rx:"20",ry:"20",fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"32"},null,-1),S("rect",{x:"48",y:"288",width:"176",height:"176",rx:"20",ry:"20",fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"32"},null,-1),S("rect",{x:"288",y:"288",width:"176",height:"176",rx:"20",ry:"20",fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"32"},null,-1)]))}}),tt={xmlns:"http://www.w3.org/2000/svg","xmlns:xlink":"http://www.w3.org/1999/xlink",viewBox:"0 0 512 512"},rt=L({name:"LayersOutline",render:function(r,o){return E(),j("svg",tt,o[0]||(o[0]=[S("path",{d:"M434.8 137.65l-149.36-68.1c-16.19-7.4-42.69-7.4-58.88 0L77.3 137.65c-17.6 8-17.6 21.09 0 29.09l148 67.5c16.89 7.7 44.69 7.7 61.58 0l148-67.5c17.52-8 17.52-21.1-.08-29.09z",fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"32"},null,-1),S("path",{d:"M160 308.52l-82.7 37.11c-17.6 8-17.6 21.1 0 29.1l148 67.5c16.89 7.69 44.69 7.69 61.58 0l148-67.5c17.6-8 17.6-21.1 0-29.1l-79.94-38.47",fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"32"},null,-1),S("path",{d:"M160 204.48l-82.8 37.16c-17.6 8-17.6 21.1 0 29.1l148 67.49c16.89 7.7 44.69 7.7 61.58 0l148-67.49c17.7-8 17.7-21.1.1-29.1L352 204.48",fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"32"},null,-1)]))}}),nt={xmlns:"http://www.w3.org/2000/svg","xmlns:xlink":"http://www.w3.org/1999/xlink",viewBox:"0 0 512 512"},lt=L({name:"LogOutOutline",render:function(r,o){return E(),j("svg",nt,o[0]||(o[0]=[S("path",{d:"M304 336v40a40 40 0 0 1-40 40H104a40 40 0 0 1-40-40V136a40 40 0 0 1 40-40h152c22.09 0 48 17.91 48 40v40",fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"32"},null,-1),S("path",{fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"32",d:"M368 336l80-80l-80-80"},null,-1),S("path",{fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"32",d:"M176 256h256"},null,-1)]))}}),it={xmlns:"http://www.w3.org/2000/svg","xmlns:xlink":"http://www.w3.org/1999/xlink",viewBox:"0 0 512 512"},at=L({name:"PersonOutline",render:function(r,o){return E(),j("svg",it,o[0]||(o[0]=[S("path",{d:"M344 144c-3.92 52.87-44 96-88 96s-84.15-43.12-88-96c-4-55 35-96 88-96s92 42 88 96z",fill:"none",stroke:"currentColor","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"32"},null,-1),S("path",{d:"M256 304c-87 0-175.3 48-191.64 138.6C62.39 453.52 68.57 464 80 464h352c11.44 0 17.62-10.48 15.65-21.4C431.3 352 343 304 256 304z",fill:"none",stroke:"currentColor","stroke-miterlimit":"10","stroke-width":"32"},null,-1)]))}}),st="/assets/barbara-logo-compact-dark-CfwBpFwl.svg",ct="/assets/barbara-logo-compact-light-DzRtE2s_.svg",dt={class:"sider-inner"},ut=["src"],vt=["src"],mt={class:"sider-footer"},ht={class:"user-profile"},pt={class:"user-avatar"},ft=["src"],gt={key:1},bt={key:0,class:"user-role-only"},xt={class:"workspace-header"},Ct={class:"breadcrumbs"},yt={class:"crumb active"},wt={class:"workspace-content"},zt={__name:"AdminLayout",setup(e){const r=mo(),o=ho(),{isDark:a}=so(),s=f(()=>a.value?go:bo),i=f(()=>a.value?st:ct),{user:d,broker:x,isAdmin:m,signOut:b}=co(),_=F(!1);uo(()=>{try{const w=localStorage.getItem("ec_sidebar_collapsed");w!==null&&(_.value=w==="1"||w==="true")}catch{}}),vo(_,w=>{try{localStorage.setItem("ec_sidebar_collapsed",w?"1":"0")}catch{}});const O=[{key:"dashboard",label:"Dashboard",icon:()=>l(D,{size:18},{default:()=>l(ot)}),to:"/dashboard"},{key:"brokers",label:"Brokers",icon:()=>l(D,{size:18},{default:()=>l(Jo)}),to:"/brokers"},{key:"leads",label:"Leads",icon:()=>l(D,{size:18},{default:()=>l(wo)}),to:"/leads"},{key:"analytics",label:"Analytics",icon:()=>l(D,{size:18},{default:()=>l(zo)}),to:"/analytics",adminOnly:!0},{key:"appointments",label:"Appointments",icon:()=>l(D,{size:18},{default:()=>l(ko)}),to:"/appointments"},{key:"verticals",label:"Verticals",icon:()=>l(D,{size:18},{default:()=>l(rt)}),to:"/verticals",adminOnly:!0},{key:"testy-control",label:"Testy Control",icon:()=>l(D,{size:18},{default:()=>l(Zo)}),to:"/testy-control",adminOnly:!0},{key:"profile",label:"Profile",icon:()=>l(D,{size:18},{default:()=>l(at)}),to:"/profile"}],h=f(()=>m.value?O:O.filter(w=>!w.adminOnly)),B={Dashboard:"dashboard",Brokers:"brokers",BrokerDetail:"brokers",Leads:"leads",LeadDetail:"leads",Analytics:"analytics",Appointments:"appointments",Verticals:"verticals",TestyControl:"testy-control",UserProfile:"profile"},T=f(()=>B[r.name]||"dashboard"),I=f(()=>({dashboard:"Dashboard",brokers:"Brokers",leads:"Leads",analytics:"Analytics",appointments:"Appointments",verticals:"Verticals","testy-control":"Testy Control",profile:"Profile"})[T.value]??"Workspace");f(()=>{var w;return((w=x.value)==null?void 0:w.contact_name)||"Admin User"});const R=f(()=>{var w,p,C,y;if((p=(w=d.value)==null?void 0:w.user_metadata)!=null&&p.display_name){const H=d.value.user_metadata.display_name.trim().split(/\s+/);return H.length>=2?(H[0][0]+H[H.length-1][0]).toUpperCase():H[0][0].toUpperCase()}if((C=x.value)!=null&&C.contact_name){const H=x.value.contact_name.trim().split(/\s+/);return H.length>=2?(H[0][0]+H[H.length-1][0]).toUpperCase():H[0][0].toUpperCase()}return(y=d.value)!=null&&y.email?d.value.email.split("@")[0][0].toUpperCase():"U"}),A=f(()=>{var w,p;return((p=(w=d.value)==null?void 0:w.user_metadata)==null?void 0:p.avatar_url)||null});function q(w,p){p!=null&&p.to&&p.to!==r.path&&o.push(p.to)}async function K(){await b(),o.push("/login")}return(w,p)=>{const C=po("router-view");return E(),Ie(U(Re),{"has-sider":"",class:"admin-shell"},{default:X(()=>[W(U(Fo),{bordered:"","collapse-mode":"width","native-scrollbar":!1,"collapsed-width":61,width:"192",collapsed:_.value,class:Se(["notion-sider",{"is-collapsed":_.value}])},{default:X(()=>[S("div",dt,[S("div",{class:Se(["workspace-brand",{"is-collapsed":_.value}]),onClick:p[0]||(p[0]=y=>_.value=!_.value)},[_.value?(E(),j("img",{key:1,src:i.value,alt:"Barbara Logo",class:"workspace-logo workspace-logo--collapsed"},null,8,vt)):(E(),j("img",{key:0,src:s.value,alt:"Barbara Logo",class:"workspace-logo"},null,8,ut))],2),W(U(Yo),{collapsed:_.value,options:h.value,value:T.value,class:"nav-menu","onUpdate:value":q},null,8,["collapsed","options","value"])]),S("div",mt,[S("div",ht,[S("div",pt,[A.value?(E(),j("img",{key:0,src:A.value,alt:"Profile",class:"avatar-image"},null,8,ft)):(E(),j("span",gt,ae(R.value),1))]),W(fo,{name:"fade"},{default:X(()=>[_.value?_e("",!0):(E(),j("div",bt,ae(U(m)?"Administrator":"Broker"),1))]),_:1})]),_.value?_e("",!0):(E(),Ie(U(Po),{key:0,quaternary:"",circle:"",size:"small",onClick:K},{default:X(()=>[W(U(D),null,{default:X(()=>[W(U(lt))]),_:1})]),_:1}))])]),_:1},8,["collapsed","class"]),W(U(Re),{class:"main-canvas"},{default:X(()=>[S("header",xt,[S("div",Ct,[S("span",yt,ae(I.value),1)]),p[1]||(p[1]=S("div",{class:"header-actions"},null,-1))]),S("main",wt,[W(C)])]),_:1})]),_:1})}}},$t=xo(zt,[["__scopeId","data-v-104fe064"]]);export{$t as default};
