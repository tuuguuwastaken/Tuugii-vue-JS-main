<template>
    <div class="container boxx">
        <form @submit.prevent="updatePost()">
            <label for="title">Title:</label>
            <input type="text" id="title" name="title" v-model="post.title" >
            <br>
            <label for="body">Body:</label>
            <textarea id="body" name="body" v-model="post.body"></textarea>
            <br>
            <button type="submit" >update post</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name:'update-main',
    components:{

    },
    data() {
        return {
            post:{
                title:'',
                body:''
            },
        }
    },
    mounted(){
        // const id = this.$route.params.id
        // axios.get(`http://127.0.0.1:5000/api/post/${id}`)
        //     .then(res =>{
        //         this.post = res.data;
        //         this.title = this.post[0][1]
        //         this.body = this.post[0][2]
        //         console.log(this.title)
        //         console.log(this.body)
        //     })
        //     .catch(err =>{
        //         alert(err)
        //     })
    },
    methods: {
        updatePost(){
            const id = this.$route.params.id
            
            axios
                .patch(`http://127.0.0.1:5000/api/update/${id}`, {
                    title: this.post.title,
                    body: this.post.body
                })
                .then(response => {
                    console.log(response.data)  
                    alert('Post updated successfully')
                    this.$router.push('/')
                })
                .catch(error => {   
                    console.log(error)
                alert('Failed to update post')
                })
            }
        }
    }

</script>

<style scoped>
    .boxx{
        background-color:#b9e3ff;
    }
    label{
        font-size:2.5rem;
    }
    #title {
        width: 100%;
        height: 40px;
        font-size: 16px;
        padding: 10px;
        border: 1px solid #4290c4;
        border-radius: 4px;
        box-sizing: border-box;
    }
    #textbody{
        width: 100%;
        height: 200px;
        font-size: 16px;
        padding: 10px;
        border: 1px solid #4290c4;
        border-radius: 4px;
        box-sizing: border-box;
    }
</style>