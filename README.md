# leave_system

注意：
    需要安装依赖包  并配置mysql数据库
 


设计思路：
	首先分析该项目用什么框架，我在这边用的是Flask
	设计数据库存储
		id ，name，start_time,end_time,reason,state,timestamp
	分析该项目需要多少接口路由：
	一个请假申请页面
		一个查询接口   '/'
		一个写入接口   '/get_user'
		一个撤销接口  '/delete_user/<id>'
	请假审批页面
		一个查询接口  '/admin'
		一个修改状态接口  '/up_type/<id>'
	
	为了前段页面效果显示的相对好点，前端页面我是下载一个模板文件，在此基础上修改完成的前端
	使用前后端不分离开发，接口返回的是静态文件，前端使用jinja2模板渲染展示
	

