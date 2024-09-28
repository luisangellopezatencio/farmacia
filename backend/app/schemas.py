from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Esquema para el inicio de sesión (recibe username y password)
class UserLoginSchema(BaseModel):
    identifier: str
    password: str

    class Config:
        orm_mode = True

class UserLoginResponseSchema(BaseModel):
    success: bool  # Indica si el inicio de sesión fue exitoso
    access_token: str  # Token de acceso
    token_type: str  # Tipo de token, generalmente "bearer"
    user: str  # El username o el email del usuario

# Esquema para los tokens (JWT)
class TokenSchema(BaseModel):
    access_token: str
    token_type: str

# Esquema para el usuario autenticado (datos a devolver después de iniciar sesión)
class UserSchema(BaseModel):
    id_user: int
    username: str
    name_user: str
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    foto: Optional[str] = None
    permisos_acceso: Optional[str] = None
    status: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class MedicamentoSchema(BaseModel):
    codigo: str
    codigo_barras: Optional[str] = None
    nombre_generico: str
    nombre_comercial: Optional[str] = None
    laboratorio: Optional[str] = None
    numero_lote: Optional[str] = None
    fecha_vencimiento: Optional[datetime] = None
    precio_compra: float
    precio_venta: float
    unidad: str
    stock: int
    created_user: int
    created_date: datetime
    updated_user: Optional[int] = None
    updated_date: Optional[datetime] = None

    class Config:
        orm_mode = True

class TransaccionMedicamentoSchema(BaseModel):
    codigo_transaccion: str
    fecha: datetime
    codigo: str
    numero: int
    created_user: int
    created_date: datetime
    tipo_transaccion: str

    class Config:
        orm_mode = True

# Esquema para la respuesta después de autenticación exitosa
class LoginResponseSchema(BaseModel):
    user: UserSchema
    token: TokenSchema
