# ToDoWoo

## Endpoints

### Todos

- **Create Todo**: `POST /api/todos/`
  - Create a new Todo item.
  - Requires authentication with a token.

- **Get Todo List**: `GET /api/todos/`
  - Get a list of all Todo items for the authenticated user.

- **Get Todo Detail**: `GET /api/todos/<int:pk>/`
  - Get details of a specific Todo item.
  - Requires authentication and ownership.

- **Update Todo**: `PUT /api/todos/<int:pk>/`
  - Update details of a specific Todo item.
  - Requires authentication and ownership.

- **Partial Update Todo**: `PATCH /api/todos/<int:pk>/`
  - Partially update details of a specific Todo item.
  - Requires authentication and ownership.

- **Delete Todo**: `DELETE /api/todos/<int:pk>/`
  - Delete a specific Todo item.
  - Requires authentication and ownership.

- **Get Completed Todos**: `GET /api/todos/completed/`
  - Get a list of completed Todo items.
  - Requires authentication.

### Users

- **Register User**: `POST /api/users/signup/`
  - Register a new user.
  - Requires a unique username and password.

- **Login User**: `POST /api/users/signin/`
  - Obtain a token for authentication.
  - Requires a valid username and password.
