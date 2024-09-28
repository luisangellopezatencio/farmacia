from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Tabla Usuarios
class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id_user = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False, unique=True)
    name_user = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    telefono = Column(String(20))
    foto = Column(String(255))
    permisos_acceso = Column(String(20))
    status = Column(String(20))
    created_at = Column(Date)
    updated_at = Column(Date)
    
    # Relación con Transacciones (Relación uno a muchos)
    transacciones = relationship("TransaccionMedicamento", back_populates="usuario_creador_transaccion")

    # Relación con Medicamentos creados por el usuario (uno a muchos)
    medicamentos_creados = relationship("Medicamento", foreign_keys='Medicamento.created_user', back_populates="usuario_creador_medicamento")

    # Relación con Medicamentos actualizados por el usuario (uno a muchos)
    medicamentos_actualizados = relationship("Medicamento", foreign_keys='Medicamento.updated_user', back_populates="usuario_actualizador_medicamento")


# Tabla Medicamentos
class Medicamento(Base):
    __tablename__ = 'medicamentos'
    
    codigo = Column(Integer, primary_key=True, index=True)
    numero = Column(String(50), nullable=False)
    codigo_barras = Column(String(50))
    nombre_generico = Column(String(100), nullable=False)
    nombre_comercial = Column(String(100))
    laboratorio = Column(String(100))
    numero_lote = Column(String(50))
    fecha_vencimiento = Column(Date)
    precio_compra = Column(Float, nullable=False)
    precio_venta = Column(Float, nullable=False)
    unidad = Column(String(20), nullable=False)
    stock = Column(Integer, nullable=False)
    created_user = Column(Integer, ForeignKey('usuarios.id_user'))
    created_date = Column(Date)
    updated_user = Column(Integer, ForeignKey('usuarios.id_user'))
    updated_date = Column(Date)
    
    # Relación con Transacciones (Relación uno a muchos)
    transacciones = relationship("TransaccionMedicamento", back_populates="medicamento")

    # Relación con el Usuario que creó el medicamento
    usuario_creador_medicamento = relationship("Usuario", foreign_keys=[created_user], back_populates="medicamentos_creados")

    # Relación con el Usuario que actualizó el medicamento
    usuario_actualizador_medicamento = relationship("Usuario", foreign_keys=[updated_user], back_populates="medicamentos_actualizados")


# Tabla Transacción Medicamentos
class TransaccionMedicamento(Base):
    __tablename__ = 'transaccion_medicamentos'
    
    codigo_transaccion = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False)
    codigo = Column(Integer, ForeignKey('medicamentos.codigo'))
    numero = Column(Integer)
    created_user = Column(Integer, ForeignKey('usuarios.id_user'))
    created_date = Column(Date)
    tipo_transaccion = Column(String(50), nullable=False)
    
    # Relación con Medicamento (Relación muchos a uno)
    medicamento = relationship("Medicamento", back_populates="transacciones")
    
    # Relación con Usuario (Relación muchos a uno)
    usuario_creador_transaccion = relationship("Usuario", back_populates="transacciones")

