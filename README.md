Admin panel to manage companies
Basically, project to manage companies and their employees. Mini-CRM.
• Basic Laravel Auth: ability to log in as administrator
• Use database seeds to create first user with email admin@admin.com and password “password”
• CRUD functionality (Create / Read / Update / Delete) for two menu items: Companies and
Employees.
• Companies DB table consists of these fields: Name (required), email, logo (minimum 100×100),
website
• Employees DB table consists of these fields: First name (required), last name (required),
Company (foreign key to Companies), email, phone
• Use database migrations to create those schemas above
• Store companies logos in storage/app/public folder and make them accessible from public
• Use basic Laravel resource controllers with default methods – index, create, store etc.
• Use Laravel’s validation function, using Request classes
• Use Laravel’s pagination for showing Companies/Employees list, 10 entries per page
• Use Laravel 8 bootstrap auth as default Bootstrap-based design theme, but remove ability to
register

Basically, that’s it. With this simple exercise junior developer shows the skills in basic Laravel things:
• MVC
• Auth
• CRUD and Resource Controllers
• Eloquent and Relationships
• Database migrations and seeds
• Form Validation and Requests
• File management
• Basic Bootstrap front-end
• Pagination