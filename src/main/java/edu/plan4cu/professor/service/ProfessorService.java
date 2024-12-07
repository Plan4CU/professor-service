package edu.plan4cu.professor.service;

import edu.plan4cu.professor.entity.Professor;
import edu.plan4cu.professor.repository.ProfessorRepository;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

@Service
public class ProfessorService {
    private final ProfessorRepository professorRepository;

    public ProfessorService(ProfessorRepository professorRepository) {
        this.professorRepository = professorRepository;
    }

    public Page<Professor> getAllProfessors(Pageable pageable) {
        return professorRepository.findAll(pageable);
    }

    public Professor getProfessorById(String id) {
        return professorRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Professor not found"));
    }

    public Professor createProfessor(Professor professor) {
        if (professor.getId() == null || professor.getId().isEmpty()) {
            throw new IllegalArgumentException("ID must be provided when creating a new Professor");
        }
        return professorRepository.save(professor);
    }

    public Professor updateProfessor(String id, Professor professor) {
        if (!professorRepository.existsById(id)) {
            throw new RuntimeException("Professor not found");
        }
        professor.setId(id);
        return professorRepository.save(professor);
    }

    public void deleteProfessor(String id) {
        professorRepository.deleteById(id);
    }
}
