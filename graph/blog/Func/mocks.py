# -*- coding: utf-8 -*-


class Post:
    
    def __init__(self):
    
        self.POSTS = [
                    {'id' : 1, 'title' : 'First post', 'body' : 'I write the first post'},
                    {'id' : 2, 'title' : 'Second post', 'body' : 'I write the second post'},
                    {'id' : 3, 'title' : 'Third post', 'body' : 'I write the third post'},
                    ]
    
    
    
    def all(self):
        return self.POSTS
        
        
    def find(self, id):
        try:
            return self.POSTS[int(id)-1]
        except:
            raise Http404('no article ' + id )


django.__version__