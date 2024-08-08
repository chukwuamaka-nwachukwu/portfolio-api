from flask import request, jsonify
from app import app
from models import db, Project, BlogPost, Contact


@app.route('/projects', methods=['POST'])
def add_project():
    data = request.get_json()
    new_project = Project(title=data['title'], description=data['description'], link=data.get('link'))
    db.session.add(new_project)
    db.session.commit()
    return jsonify({"MESSAGE": "PROJECT ADDED SUCCESSFULLY"}), 201

@app.route('/projects/<int:id>', methods=['PUT'])
def edit_project(id):
    data = request.get_json()
    project = Project.query.get_or_404(id)
    project.title = data['title']
    project.description = data['description']
    project.link = data.get('link')
    db.session.commit()
    return jsonify({"MESSAGE": "PROJECT UPDATED SUCCESSFULLY"})

@app.route('/projects/<int:id>', methods=['DELETE'])
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({"MESSAGE": "PROJECT DELETED SUCCESSFULLY"})

@app.route('/projects', methods=['GET'])
def get_all_projects():
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects])

@app.route('/projects/<int:id>', methods=['GET'])
def get_single_project(id):
    project = Project.query.get_or_404(id)
    return jsonify(project.to_dict())


@app.route('/blogposts', methods=['POST'])
def add_blog_post():
    data = request.get_json()
    new_blog_post = BlogPost(title=data['title'], content=data['content'])
    db.session.add(new_blog_post)
    db.session.commit()
    return jsonify({"MESSAGE": "BLOG POST ADDED SUCCESSFULLY"}), 201

@app.route('/blogposts/<int:id>', methods=['PUT'])
def edit_blog_post(id):
    data = request.get_json()
    blog_post = BlogPost.query.get_or_404(id)
    blog_post.title = data['title']
    blog_post.content = data['content']
    db.session.commit()
    return jsonify({"MESSAGE": "BLOG POST UPDATED SUCCESSFULLY"})

@app.route('/blogposts/<int:id>', methods=['DELETE'])
def delete_blog_post(id):
    blog_post = BlogPost.query.get_or_404(id)
    db.session.delete(blog_post)
    db.session.commit()
    return jsonify({"MESSAGE": "BLOG POST DELETED SUCCESSFULLY"})

@app.route('/blogposts', methods=['GET'])
def get_all_blog_posts():
    blog_posts = BlogPost.query.all()
    return jsonify([blog_post.to_dict() for blog_post in blog_posts])

@app.route('/blogposts/<int:id>', methods=['GET'])
def get_single_blog_post(id):
    blog_post = BlogPost.query.get_or_404(id)
    return jsonify(blog_post.to_dict())

# Contact Endpoints
@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    new_contact = Contact(name=data['name'], email=data['email'], message=data['message'])
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({"MESSAGE": "CONTACT ADDED SUCCESSFULLY"}), 201

@app.route('/contacts/<int:id>', methods=['PUT'])
def edit_contact(id):
    data = request.get_json()
    contact = Contact.query.get_or_404(id)
    contact.name = data['name']
    contact.email = data['email']
    contact.message = data['message']
    db.session.commit()
    return jsonify({"MESSAGE": "CONTACT UPDATED SUCCESSFULLY"})

@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"MESSAGE": "CONTACT DELETED SUCCESSFULLY "})

@app.route('/contacts', methods=['GET'])
def get_all_contacts():
    contacts = Contact.query.all()
    return jsonify([contact.to_dict() for contact in contacts])

@app.route('/contacts/<int:id>', methods=['GET'])
def get_single_contact(id):
    contact = Contact.query.get_or_404(id)
    return jsonify(contact.to_dict())
