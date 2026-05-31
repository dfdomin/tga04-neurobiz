import assert from "node:assert/strict";
import { parseAcademusoftStudents } from "../js/import-students.mjs";

const groupOneText = `
Listado de Estudiantes Inscritos

Materia                                                                      Grupo
TGA04-FUNDAMENTOS DE COMPUTACION PARA LOS NEGOCIOS                          6_GA_G1

No.                      Documento                           Codigo                                  Nombre Completo
1                      CC - 1000000001                   1000000001                       PRUEBA UNO ANA MARIA
2                      CC - 1000000002                   1000000002                       PRUEBA DOS CARLOS JOSE
12                     CC - 1000000012                   0                                PRUEBA DOCE CODIGO CERO
25                     CC - 1000000025                   1000000025                       PRUEBA VEINTICINCO FINAL
`;

const groupTwoText = `
Materia                                                                        Grupo
TGA04-FUNDAMENTOS DE COMPUTACION PARA LOS NEGOCIOS                             6_GA_G2

No.                         Documento                               Codigo                                 Nombre Completo
3                         TI - 2000000003                        2000000003                        EJEMPLO TRES NOMBRE FICTICIO
8                         CC - 2000000008                        0                                 EJEMPLO OCHO CODIGO CERO
28                        CC - 2000000028                        2000000028                        EJEMPLO VEINTIOCHO FINAL
`;

const legacyText = `
GRUPO: 6_GA_G3
1  ESTUDIANTE PRUEBA UNO  3000000001
2  ESTUDIANTE PRUEBA DOS
3000000002
`;

{
  const result = parseAcademusoftStudents(groupOneText);
  assert.equal(result.students.length, 4);
  assert.equal(result.meta.grupo, "6_GA_G1");
  assert.deepEqual(result.students[2], {
    name: "PRUEBA DOCE CODIGO CERO",
    cc: "1000000012",
    grupo: "6_GA_G1",
    horario: "",
  });
}

{
  const result = parseAcademusoftStudents(groupTwoText);
  assert.equal(result.students.length, 3);
  assert.equal(result.meta.grupo, "6_GA_G2");
  assert.equal(result.students[0].cc, "2000000003");
  assert.equal(result.students[0].name, "EJEMPLO TRES NOMBRE FICTICIO");
  assert.equal(result.students[1].cc, "2000000008");
}

{
  const result = parseAcademusoftStudents(legacyText);
  assert.equal(result.students.length, 2);
  assert.equal(result.meta.grupo, "6_GA_G3");
  assert.equal(result.students[1].name, "ESTUDIANTE PRUEBA DOS");
  assert.equal(result.students[1].cc, "3000000002");
}

console.log("import-students-parser tests passed");
