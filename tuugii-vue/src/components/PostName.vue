<template>
    <div class="container">
        <div class="post-title">
            <h3>{{ this.postID }} : {{ this.postTitle }}</h3>
        </div>
        <div class="body-container btn-comment">
            <h3 class="body-text">{{ this.body }}</h3>
            <button class="btn btn-comments" style="background-color: red" @click="deletePost(this.postID)">delete</button>
            <button class="btn btn-comments" style="background-color: grey" @click="$router.push('/update/'+this.postID)">update</button>
            
            <!-- <div v-if="showComment">
                <div v-for="comment in comments" :key="comment.id" class="Comments">
                    <hr/>
                    <h4>{{ comment.name }}</h4>
                    <p><strong>{{ comment.email }}</strong></p>
                    <p>{{ comment.body }}</p>
                </div>
            </div> -->
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default{
        name:"Post-titles",
        components:{
        },
        data(){
            return{
                showdropdown: false,
                showComment: false,
                comments:[]
            }
        },
        props:{
            postTitle: String,
            postID : String,
            body: String,
        },
        methods:{
            ToggleDropdown(button){
                if(this.showdropdown && this.button === this.button){
                    this.showdropdown = false;
                } else{
                    this.showdropdown = true;
                    this.button = button
                }
            },
            getComments(postID){
                axios.get(`https://jsonplaceholder.typicode.com/comments?postId=${postID}`)
                    .then(results =>{
                        this.comments = results.data;
                    })
                    .catch(err =>{
                        console.log(err)
                    })
            },
            deletePost(id){
                axios.delete(`http://127.0.0.1:5000/api/delete/${id}`)
                    .then(res =>{
                        console.log(res)
                        alert("succesfully deleted")
                        window.location.reload()
                    })
                    .catch(err=>{
                        alert(err)
                    })
            }
        }
    }
</script>

<style scoped>
    .comments{
        margin: 0px,5px,12px,5px;
    }
    .btn-comments{
        margin-top:10px;
    }
    .btn{
        background-color:rgb(10, 110, 192);
    }
    p{
        margin-top:0.5rem;
    }
    .post-title{
        display: flex;
        justify-content: space-between;
        align-items:flex-start;
    }
    .container{
        
        font-size: 20px;
        text-align: left;
        border: 1px solid rgb(130, 196, 235);
        margin-bottom: 4px;
        padding: 9px;
        border-radius: 12px;
    }
    h4{
    font-size: 18px;
    }
    p{
        font-size: 14px;
    }
    .body-text{
        font-size: 20px;
        font-weight: lighter;
    }

</style>