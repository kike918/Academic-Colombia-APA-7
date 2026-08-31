# Arquitectura

## Fuente de verdad
GitHub debe ser la fuente canónica.

## Capas

### Core
Reglas neutrales de plataforma.

### Institutions
Reglas específicas UNAD/SENA.

### Skills
Workflows pequeños, reutilizables y combinables.

### Platform adapters
Configuraciones específicas para Custom GPT y Gemini Gem.

## Política de actualización

1. Cambiar primero el core o skill correspondiente.
2. Actualizar VERSION y CHANGELOG.
3. Probar en ChatGPT.
4. Sincronizar adapter de GPT.
5. Cuando esté estable, sincronizar Gemini.
6. Registrar diferencias inevitables entre plataformas.

## SemVer
- PATCH: correcciones de redacción o QA sin cambio de comportamiento.
- MINOR: nueva regla, workflow o perfil compatible.
- MAJOR: cambio de jerarquía, contrato o comportamiento incompatible.
