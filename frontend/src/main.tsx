import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { store } from "./app/store"; // Importa tu store
import LoginView from "./views/loginView";
import "./index.css";

const router = createBrowserRouter([
  {
    path: "/",
    element: <LoginView/>,
  },
]);

createRoot(document.getElementById("root")!).render(
  <Provider store={store}>
    <StrictMode>
      <RouterProvider router={router} />
    </StrictMode>
  </Provider>
);
