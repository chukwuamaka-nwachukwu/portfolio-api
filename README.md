# Portfolio API

This API provides endpoints for managing projects, blogging posts, and providing contact information for a personal portfolio website.

## The Endpoints

### The Projects
- **POST /projects**: This is to add a new project.
- **PUT /projects/<id>**: This is to edit an already existing project.
- **DELETE /projects/<id>**: This is to delete an existing project.
- **GET /projects**: This is to get all projects.
- **GET /projects/<id>**: This is to get a single project by using the ID.

### The Blog Posts
- **POST /blogposts**: This is to add a new blog post.
- **PUT /blogposts/<id>**: This is to edit an already existing blog post.
- **DELETE /blogposts/<id>**: This is to delete a blog post.
- **GET /blogposts**: This is to get all blog posts.
- **GET /blogposts/<id>**: This is to get a single blog post by using the ID.

### The Contacts
- **POST /contacts**: This is to add new contact information.
- **PUT /contacts/<id>**: This is to edit an already existing contact information.
- **DELETE /contacts/<id>**: This is to delete contact information.
- **GET /contacts**: This is to get all contact information.
- **GET /contacts/<id>**: This is to get a single contact by using the ID.

## Setup

1. Install the required packages:
   ```sh
   pip install -r requirements.txt
