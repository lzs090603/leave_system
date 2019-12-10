var vm = new Vue({
    el: '#app',
    data: {
        host, 
        user_name: '',
        star_time: '',
        end_time: '',
        reason: "",
        state: "",
        
        
    },
    mounted: function(){
        axios.get('http://127.0.0.1:5000'+ '/table/', {
                responseType: 'json',
            })
            .then(response => {
                // 加载用户数据
                this.user_name = response.data.user_name;
                this.star_time = response.data.star_time;
                this.end_time = response.data.end_time;
                this.reason = response.data.reason;
                this.state = response.data.state;
            })
            .catch(error => {
                if (error.response.status==401 || error.response.status==403) {
                    location.href = 'tables.html';
                }
            });
         
    },
    methods: {
        // post
        post_from: function(){
            axios.post(this.host + '/post/', { 
                responseType: 'json',
            })
            .then(response => {
                // 加载用户数据
                this.user_name = this.user_name;
                this.star_time = this.star_time;
                this.end_time = this.end_time;
                this.reason = this.reason;
                this.state = this.state;
            })
            .catch(error => {
                if (error.response.status==401 || error.response.status==403) {
                    location.href = 'tables.html';
                }
            });
        },
        
        
    }
});