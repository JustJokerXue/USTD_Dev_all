console.log('非源码，仅用作演示。下载源码请访问：https://www.17sucai.com');/* Copyright (c) 2011 Piotr Rochala (http://rocha.la)
 * Dual licensed under the MIT (http://www.opensource.org/licenses/mit-license.php)
 * and GPL (http://www.opensource.org/licenses/gpl-license.php) licenses.
 *
 * Version: 1.3.6
 *
 */
(function(a){a.fn.extend({slimScroll:function(d){var b={width:"auto",height:"250px",size:"7px",color:"#000",position:"right",distance:"1px",start:"top",opacity:0.4,alwaysVisible:false,disableFadeOut:false,railVisible:false,railColor:"#333",railOpacity:0.2,railDraggable:true,railClass:"slimScrollRail",barClass:"slimScrollBar",wrapperClass:"slimScrollDiv",allowPageScroll:false,wheelStep:20,touchScrollStep:200,borderRadius:"7px",railBorderRadius:"7px"};var c=a.extend(b,d);this.each(function(){var o,n,m,w,B,h,u,p,i="<div></div>",r=30,y=false;var q=a(this);if(q.parent().hasClass(c.wrapperClass)){var s=q.scrollTop();g=q.closest("."+c.barClass);x=q.closest("."+c.railClass);j();if(a.isPlainObject(d)){if("height" in d&&d.height=="auto"){q.parent().css("height","auto");q.css("height","auto");var k=q.parent().parent().height();q.parent().css("height",k);q.css("height",k)}if("scrollTo" in d){s=parseInt(c.scrollTo)}else{if("scrollBy" in d){s+=parseInt(c.scrollBy)}else{if("destroy" in d){g.remove();x.remove();q.unwrap();return}}}z(s,false,true)}return}else{if(a.isPlainObject(d)){if("destroy" in d){return}}}c.height=(c.height=="auto")?q.parent().height():c.height;var C=a(i).addClass(c.wrapperClass).css({position:"relative",overflow:"hidden",width:c.width,height:c.height});q.css({overflow:"hidden",width:c.width,height:c.height});var x=a(i).addClass(c.railClass).css({width:c.size,height:"100%",position:"absolute",top:0,display:(c.alwaysVisible&&c.railVisible)?"block":"none","border-radius":c.railBorderRadius,background:c.railColor,opacity:c.railOpacity,zIndex:90});var g=a(i).addClass(c.barClass).css({background:c.color,width:c.size,position:"absolute",top:0,opacity:c.opacity,display:c.alwaysVisible?"block":"none","border-radius":c.borderRadius,BorderRadius:c.borderRadius,MozBorderRadius:c.borderRadius,WebkitBorderRadius:c.borderRadius,zIndex:99});var v=(c.position=="right")?{right:c.distance}:{left:c.distance};x.css(v);g.css(v);q.wrap(C);q.parent().append(g);q.parent().append(x);if(c.railDraggable){g.bind("mousedown",function(E){var D=a(document);m=true;t=parseFloat(g.css("top"));pageY=E.pageY;D.bind("mousemove.slimscroll",function(F){currTop=t+F.pageY-pageY;g.css("top",currTop);z(0,g.position().top,false)});D.bind("mouseup.slimscroll",function(F){m=false;l();D.unbind(".slimscroll")});return false}).bind("selectstart.slimscroll",function(D){D.stopPropagation();D.preventDefault();return false})}x.hover(function(){A()},function(){l()});g.hover(function(){n=true},function(){n=false});q.hover(function(){o=true;A();l()},function(){o=false;l()});q.bind("touchstart",function(E,D){if(E.originalEvent.touches.length){B=E.originalEvent.touches[0].pageY}});q.bind("touchmove",function(E){if(!y){E.originalEvent.preventDefault()}if(E.originalEvent.touches.length){var D=(B-E.originalEvent.touches[0].pageY)/c.touchScrollStep;z(D,true);B=E.originalEvent.touches[0].pageY}});j();if(c.start==="bottom"){g.css({top:q.outerHeight()-g.outerHeight()});z(0,true)}else{if(c.start!=="top"){z(a(c.start).position().top,null,true);if(!c.alwaysVisible){g.hide()}}}f(this);function e(E){if(!o){return}var E=E||window.event;var D=0;if(E.wheelDelta){D=-E.wheelDelta/120}if(E.detail){D=E.detail/3}var F=E.target||E.srcTarget||E.srcElement;if(a(F).closest("."+c.wrapperClass).is(q.parent())){z(D,true)}if(E.preventDefault&&!y){E.preventDefault()}if(!y){E.returnValue=false}}function z(I,F,E){y=false;var D=I;var G=q.outerHeight()-g.outerHeight();if(F){D=parseInt(g.css("top"))+I*parseInt(c.wheelStep)/100*g.outerHeight();D=Math.min(Math.max(D,0),G);D=(I>0)?Math.ceil(D):Math.floor(D);g.css({top:D+"px"})}u=parseInt(g.css("top"))/(q.outerHeight()-g.outerHeight());D=u*(q[0].scrollHeight-q.outerHeight());if(E){D=I;var H=D/q[0].scrollHeight*q.outerHeight();H=Math.min(Math.max(H,0),G);g.css({top:H+"px"})}q.scrollTop(D);q.trigger("slimscrolling",~~D);A();l()}function f(D){if(window.addEventListener){D.addEventListener("DOMMouseScroll",e,false);D.addEventListener("mousewheel",e,false)}else{document.attachEvent("onmousewheel",e)}}function j(){h=Math.max((q.outerHeight()/q[0].scrollHeight)*q.outerHeight(),r);g.css({height:h+"px"});var D=h==q.outerHeight()?"none":"block";g.css({display:D})}function A(){j();clearTimeout(w);if(u==~~u){y=c.allowPageScroll;if(p!=u){var D=(~~u==0)?"top":"bottom";q.trigger("slimscroll",D)}}else{y=false}p=u;if(h>=q.outerHeight()){y=true;return}g.stop(true,true).fadeIn("fast");if(c.railVisible){x.stop(true,true).fadeIn("fast")}}function l(){if(!c.alwaysVisible){w=setTimeout(function(){if(!(c.disableFadeOut&&o)&&!n&&!m){g.fadeOut("slow");x.fadeOut("slow")}},1000)}}});return this}});a.fn.extend({slimscroll:a.fn.slimScroll})})(jQuery);console.log('非源码，仅用作演示。下载源码请访问：https://www.17sucai.com');