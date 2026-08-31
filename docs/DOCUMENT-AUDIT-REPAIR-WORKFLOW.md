# Document Audit → Repair Workflow

## Propósito
Definir el flujo end-to-end para auditar y regenerar documentos académicos sin mezclar diagnóstico, corrección mecánica y decisiones de contenido.

## Pipeline

```text
Documento original
      ↓
academic-requirements-analyzer
      ↓
academic-document-auditor
      ↓
Matriz de hallazgos
      ↓
┌──────────────────┬────────────────────┬──────────────────┐
│ SAFE_AUTOFIX     │ EVIDENCE_REQUIRED  │ CONTENT_DECISION │
└──────────────────┴────────────────────┴──────────────────┘
      ↓
academic-document-repair
      ↓
artifact / APA / institutional QA
      ↓
render → visual inspection → iterate
      ↓
academic-final-review
      ↓
Documento corregido + reporte
```

## Regla por defecto
Si el documento ya fue evaluado positivamente en contenido, usar `conservative` salvo instrucción contraria.

## Conservative repair
Puede corregir:
- sangría francesa;
- márgenes, fuente, interlineado, alineación y espaciado;
- encabezado `Referencias`;
- convenciones de citación institucional inequívocas;
- estilos Word;
- captions y TOC cuando la corrección sea puramente mecánica;
- enlaces rotos solo si existe destino verificado.

No puede:
- añadir evidencia no verificada;
- insertar citas por semejanza temática;
- eliminar referencias huérfanas automáticamente;
- atribuir tablas sin procedencia demostrable;
- modificar conclusiones, datos o argumentos.

## Evidence-backed repair
Se activa cuando las fuentes han sido verificadas. Permite resolver:
- citas faltantes;
- notas/fuentes de tablas y figuras;
- metadatos bibliográficos incompletos;
- URL/DOI específicos;
- correspondencia cita ↔ referencia.

## Full revision
Solo con autorización explícita o cuando guía/rúbrica obliguen a modificar contenido/estructura.

## QA obligatorio para DOCX
1. Auditoría estructural.
2. Guardar copia nueva.
3. Renderizar todas las páginas.
4. Inspeccionar visualmente cada página.
5. Corregir defectos.
6. Re-renderizar.
7. Ejecutar revisión final.

## Principio de reversibilidad
El original se conserva. Toda regeneración crea una nueva versión y reporta cambios aplicados y pendientes.
