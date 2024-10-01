import { CiUser } from "react-icons/ci";
import { CiLock } from "react-icons/ci";
import { CiLogin } from "react-icons/ci";

export default function LoginView() {
  return (
    <div className="w-screen h-screen flex justify-center items-center">
      <div className="h-1/2 w-1/2 md:w-1/3 p-10 border border-gray-300 rounded shadow">
        <header className="text-2xl font-bold text-blue-900 text-center mb-8">
          Iniciar Sesión
        </header>
        <form action="iniciar-sesion">
          <label htmlFor="email-username">
            <p className="text-blue-900 font-bold text-sm mb-2">
              Nombre de usuario o correo
            </p>
            <div className="flex space-x-2 items-center border border-blue-300 rounded px-2 mb-4">
              <CiUser className="text-blue-900" />
              <input
                type="text"
                name="email-username"
                id="email-username"
                placeholder="Nombre de usuario o correo"
                className="w-full outline-none"
              />
            </div>
          </label>
          <label htmlFor="contrasena">
            <p className="text-blue-900 font-bold text-sm mb-2">Contrasena</p>
            <div className="flex space-x-2 items-center border border-blue-300 rounded px-2 mb-4">
              <CiLock className="text-blue-900" />
              <input
                type="password"
                name="contrasena"
                id="contrasena"
                className="w-full outline-none"
              />
            </div>
          </label>
          <button type="button" className="bg-blue-900 text-white px-4 py-2 rounded flex justify-center items-center space-x-2 w-full mb-2">
            <CiLogin />
            <p>Ingresar</p>
          </button>
        </form>

        <button type="button" className="text-blue-500 text-xs">
          <a href="#">
            ¿Problemas para iniciar sesión? Contacta al administrador
          </a>
        </button>
      </div>
    </div>
  );
}
