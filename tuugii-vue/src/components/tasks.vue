<template>
    <div class="container">
        <div v-for="post in posts" :key="post.id">
            <PostName :postID="post[0]" :postTitle="post[1]" :body="post[2]" />
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import PostName from './PostName.vue';
    export default{
        name:'tasks-main',
        props:{
        },
        components:{
            PostName
        },
        data(){
            return{
                posts:[],
                comments:[]
            }
        },
        mounted(){
            axios.get('http://127.0.0.1:5000/api/posts')
                .then(res =>{
                    this.posts = res.data;
                })
                .catch(err =>{
                    alert(err)
                })

            window.addEventListener('scroll', this.handleScroll);

            const scrollPosition = localStorage.getItem('scrollPosition');
            if (scrollPosition) {
            window.scrollTo(0, scrollPosition);
            localStorage.removeItem('scrollPosition');
            }
        },
        beforeUnmount() {
            window.removeEventListener('scroll', this.handleScroll);
        },
        methods:{
            handleScroll() {
                localStorage.setItem('scrollPosition', window.pageYOffset);
            }
        }
    }
</script>

<style scoped>
    h3{
        font-size: 22px;
        text-align: center;
        border: 1px solid rgb(130, 196, 235);
        margin-bottom: 4px;
        padding: 9px;
        border-radius: 12px;
    }
    h3:hover{
        transform: scale(1.1);
        cursor: pointer;
    }
    .fas {
        color: red;
    }
    .task {
        background: #f4f4f4;
        margin: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }
    .task.reminder {
        border-left: 5px solid green;
    }
    .task h3 {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .container {
        max-width: 800px;
        margin: 30px auto;
        overflow: auto;
        min-height: 300px;
        border: 1px solid steelblue;
        padding: 30px;
        border-radius: 5px;
        
    }

</style>    