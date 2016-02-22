
(function($) {
	$.fn.slideBox = function(options) {
		//默认参数
		var defaults = {
			direction : 'left',//left,top
			duration : 0.6,//unit:seconds
			easing : 'swing',//swing,linear
			delay : 3,//unit:seconds
			startIndex : 0,
			hideClickBar : false,
			clickBarRadius :5,//unit:px
			hideBottomBar : false
		};
		var settings = $.extend(defaults, options || {});// 合并defaults和options的值,生成的新对象赋值给settings,并不修改defaults和options,如果options不存在就用{}代替
		//计算相关数据
		var wrapper = $(this), ul = wrapper.children('ul.items'), lis = ul.find('li'), firstPic = lis.first().find('img');
		//好难理解wrapper是什么呢?调用时这样写的:$('#slide_div'),,,wrapper就是这个slide_div
		//找到ul,找到里面的li->lis,找到第一个图片->firstPic
		var li_num = lis.size(), li_height = 0, li_width = 0;//li可以定义宽高?
		//alert(li_num);元素个数 从1开始
		//初始化
		var init = function(){//初始化方法
			if(!wrapper.size()) return false;
			wrapper.data('over', 0);//这句什么意思呢...//向被选元素附加数据。语法:$(selector).data(name,value) 参数:name	必需。规定要设置的数据的名称。 value	必需。规定要设置的数据的值。
			
			li_height = lis.first().height();//取得图片的高
			li_width = lis.first().width();//图片的宽
			
			wrapper.css({width: li_width+'px', height:li_height+'px'});//设置slide_div的宽高=图片的宽高
			lis.css({width: li_width+'px', height:li_height+'px'});//设置每个li的宽高=图片的宽高,li是块级元素,可以设置宽高
			
			ul.append(ul.find('li:first').clone());//ul里面添加了一个li, ul里面的第一个li的复制
			li_num += 1;//xxxxx因为li_num从0开始计算的,所以加一变成从1开始计算??xxxxxx这个理解错误,为什么要+1呢?
			
			if (settings.direction == 'left') {//计算图层的偏移量
				ul.css('width', li_num * li_width + 'px');//水平偏移
			} else {
				ul.css('height', li_num * li_height + 'px');//垂直偏移
			}			
			ul.find('li:eq('+settings.startIndex+')').addClass('active');//给开始元素添加active class
			
			if(!settings.hideBottomBar){//显示tips 则运行下面的代码,生成tips.
				var tips = $('<div class="tips"></div>').css('opacity', 1).appendTo(wrapper);//先生成一个父元素,tips div
				var title = $('<div class="title"></div>').html(function(){//生成一个title div ,里面添加了html内容
					var active = ul.find('li.active').find('a'), text = active.attr('title'), href = active.attr('href');//找到a标签的title和href的内容
					return $('<a>').attr('href', href).text(text);//生成一个a标签,添加了上面找到的属性,并返回去作为title div的html内容.
				}).appendTo(tips);//把有了title内容,href内容的titlediv 添加到tips div中.
				var nums = $('<div class="nums"></div>').hide().appendTo(tips);
				lis.each(function(i, n) {//这里的i和n是什么呢? 语法:$(selector).each(function(index,element));index - 选择器的 index 位置;element - 当前的元素（也可使用 "this" 选择器）
					var a = $(n).find('a'), text = a.attr('title'), href = a.attr('href'), css = '';
					//i == settings.startIndex && (css = 'active');//这句什么用?注释掉 好像没有什么影响啊
					$('<a>').attr('href', href).text(i+1).addClass(css).css('borderRadius', settings.clickBarRadius+'px').mouseover(function(){//text(text)改成了text(i+1)
						wrapper.data('over', 1);//向被选元素附加数据。语法:$(selector).data(name,value) 参数:name	必需。规定要设置的数据的名称。 value	必需。规定要设置的数据的值。
						$(this).addClass('active').siblings().removeClass('active');
						//siblings() 获得匹配集合中每个元素的同胞，通过选择器进行筛选是可选的。例如:查找每个 p 元素的所有类名为 "selected" 的所有同胞元素：$("p").siblings(".selected")
						ul.find('li:eq('+$(this).index()+')').addClass('active').siblings().removeClass('active');
						start();
					}).appendTo(nums);
				});
			
				if(settings.hideClickBar){
					tips.hover(function(){
						nums.animate({top: '0px'}, 'fast');
					}, function(){
						nums.animate({top: tips.height()+'px'}, 'fast');
					});
					nums.show().delay(2000).animate({top: tips.height()+'px'}, 'fast');
				}else{
					nums.show();
				}
			}
			
			lis.size()>1 && start();
		};//初始化方法结束
		//开始轮播
		var start = function() {
			var active = ul.find('li.active'), active_a = active.find('a');
			var index = active.index();
			if(settings.direction == 'left'){
				offset = index * li_width * -1;
				param = {'left':offset + 'px' };
			}else{
				offset = index * li_height * -1;
				param = {'top':offset + 'px' };
			}
			
			wrapper.find('.nums').find('a:eq('+index+')').addClass('active').siblings().removeClass('active');
			wrapper.find('.title').find('a').attr('href', active_a.attr('href')).text(active_a.attr('title'));


			ul.stop().animate(param, settings.duration*1000, settings.easing, function() {
				active.removeClass('active');
				if(active.next().size()==0){
					ul.css({top:0, left:0}).find('li:eq(1)').addClass('active');
					wrapper.find('.nums').find('a:first').addClass('active').siblings().removeClass('active');
				}else{
					active.next().addClass('active');
				}
				wrapper.data('over')==0 && wrapper.data('timeid', window.setTimeout(start, settings.delay*1000));
			});
		};
		//停止轮播
		var stop = function() {
			window.clearTimeout(wrapper.data('timeid'));
		};
		//鼠标经过事件
		wrapper.hover(function(){//语法:$(selector).hover(inFunction,outFunction)  参数:inFunction	必需。规定 mouseenter 事件发生时运行的函数。outFunction	可选。规定 mouseleave 事件发生时运行的函数。
			wrapper.data('over', 1);
			stop();
		}, function(){
			wrapper.data('over', 0);
			start();
		});	
		//首张图片加载完毕后执行初始化
		var imgLoader = new Image();
		imgLoader.onload = function(){
			imgLoader.onload = null;
			init();
		};
		imgLoader.src = firstPic.attr('src');
	};
})(jQuery);