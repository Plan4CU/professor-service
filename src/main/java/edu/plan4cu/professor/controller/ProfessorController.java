package edu.plan4cu.professor.controller;

import edu.plan4cu.professor.entity.Professor;
import edu.plan4cu.professor.service.ProfessorService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.web.PageableDefault;
import org.springframework.hateoas.EntityModel;
import org.springframework.hateoas.Link;
import org.springframework.hateoas.PagedModel;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.stream.Collectors;

import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.linkTo;
import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.methodOn;

@RestController
@RequestMapping("/professors")
public class ProfessorController {
    private final ProfessorService professorService;

    public ProfessorController(ProfessorService professorService) {
        this.professorService = professorService;
    }

    @GetMapping
    @PreAuthorize("hasAuthority('professor_service:read')")
    @Operation(summary = "Get all professors", security = @SecurityRequirement(name = "bearerAuth"))
    public ResponseEntity<PagedModel<EntityModel<Professor>>> getAllProfessors(
            @PageableDefault(size = 20) Pageable pageable) {
        Page<Professor> professorPage = professorService.getAllProfessors(pageable);
        List<EntityModel<Professor>> professors = professorPage.getContent().stream()
                .map(professor -> EntityModel.of(professor,
                        linkTo(methodOn(ProfessorController.class).getProfessorById(
                                professor.getId())).withSelfRel()))
                .collect(Collectors.toList());
        Link selfLink = linkTo(methodOn(ProfessorController.class).getAllProfessors(pageable)).withSelfRel();
        PagedModel.PageMetadata pageMetadata = new PagedModel.PageMetadata(
                professorPage.getSize(), professorPage.getNumber(), professorPage.getTotalElements(),
                professorPage.getTotalPages());
        PagedModel<EntityModel<Professor>> pagedModel = PagedModel.of(professors, pageMetadata, selfLink);
        if (professorPage.hasNext()) {
            pagedModel.add(linkTo(methodOn(ProfessorController.class)
                    .getAllProfessors(pageable.next())).withRel("next"));
        }
        if (professorPage.hasPrevious()) {
            pagedModel.add(linkTo(methodOn(ProfessorController.class)
                    .getAllProfessors(pageable.previousOrFirst())).withRel("prev"));
        }
        return ResponseEntity.ok(pagedModel);
    }

    @GetMapping("/{id}")
    @PreAuthorize("hasAuthority('professor_service:read')")
    @Operation(summary = "Get a professor by ID", security = @SecurityRequirement(name = "bearerAuth"))
    public ResponseEntity<EntityModel<Professor>> getProfessorById(@PathVariable String id) {
        Professor professor = professorService.getProfessorById(id);
        EntityModel<Professor> entityModel = EntityModel.of(professor,
                linkTo(methodOn(ProfessorController.class).getProfessorById(id)).withSelfRel(),
                linkTo(methodOn(ProfessorController.class).getAllProfessors(Pageable.unpaged())).withRel("professors"));
        return ResponseEntity.ok(entityModel);
    }

    @PostMapping
    @PreAuthorize("hasAuthority('professor_service:write')")
    @Operation(summary = "Create a new professor", security = @SecurityRequirement(name = "bearerAuth"))
    public ResponseEntity<EntityModel<Professor>> createProfessor(@RequestBody Professor professor) {
        Professor newProfessor = professorService.createProfessor(professor);
        EntityModel<Professor> entityModel = EntityModel.of(newProfessor,
                linkTo(methodOn(ProfessorController.class).getProfessorById(newProfessor.getId())).withSelfRel(),
                linkTo(methodOn(ProfessorController.class).getAllProfessors(Pageable.unpaged())).withRel("professors"));
        return ResponseEntity.created(
                        linkTo(methodOn(ProfessorController.class).getProfessorById(newProfessor.getId())).toUri())
                .body(entityModel);
    }

    @PutMapping("/{id}")
    @PreAuthorize("hasAuthority('professor_service:write')")
    @Operation(summary = "Update a professor", security = @SecurityRequirement(name = "bearerAuth"))
    public ResponseEntity<EntityModel<Professor>> updateProfessor(@PathVariable String id,
            @RequestBody Professor professor) {
        Professor updatedProfessor = professorService.updateProfessor(id, professor);
        EntityModel<Professor> entityModel = EntityModel.of(updatedProfessor,
                linkTo(methodOn(ProfessorController.class).getProfessorById(id)).withSelfRel(),
                linkTo(methodOn(ProfessorController.class).getAllProfessors(Pageable.unpaged())).withRel("professors"));
        return ResponseEntity.ok(entityModel);
    }

    @DeleteMapping("/{id}")
    @PreAuthorize("hasAuthority('professor_service:write')")
    @Operation(summary = "Delete a professor", security = @SecurityRequirement(name = "bearerAuth"))
    public ResponseEntity<?> deleteProfessor(@PathVariable String id) {
        professorService.deleteProfessor(id);
        return ResponseEntity.noContent().build();
    }
}